# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.renderers import UnicodeJSONRenderer

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from users.models import UserSessionMapper


class TokensViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    permission_classes = (AllowAny,)
    renderer_classes = (UnicodeJSONRenderer, )
    serializer_class = AuthTokenSerializer
    model = Token
    lookup_field = 'username'

    def initial(self, request, *args, **kwargs):
        super(TokensViewSet, self).initial(request, *args, **kwargs)

        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def destroy(self, request, *args, **kwargs):
        print request.DATA
        token_obj = Token.objects.get(key=request.DATA['token'])
        user = token_obj.user
        m = None
        print user
        if not (user.username == kwargs['username']):
            Response(data={"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        mapper_obj_list = UserSessionMapper.objects.get_session_obj(user_obj=user)
        for mapper_obj in mapper_obj_list:
            m = mapper_obj
        if m is not None:
            session_key = m.session.session_key
            self._delete_sessions(session_key=session_key)
        return Response(data={"ok": "Logout ok"}, status=status.HTTP_200_OK)

    def _delete_sessions(self, session_key):
        session_obj_list = Session.objects.all().filter(session_key=session_key)
        for session_obj in session_obj_list:
            session_obj.delete()

    def create(self, request, *args, **kwargs):
        """
            Log in
        """
        print request.DATA
        serializer = self.serializer_class(data=request.DATA)

        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            id_num = serializer.object['user'].id
            return Response(data={'token': token.key, 'id': id_num}, status=status.HTTP_201_CREATED)
        return Response(data={'error': 'Check your id & password'}, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
