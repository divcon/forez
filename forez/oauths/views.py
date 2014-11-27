#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from oauth2_provider.views.base import AuthorizationView
from users.models import GardenUser
from users.serializers import UserSerializer
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.response import Response
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.decorators import action


class AuthorizationViewSet(AuthorizationView):

    def get_initial(self):
        return super(AuthorizationViewSet, self).get_initial()

    def form_valid(self, form):
        return super(AuthorizationViewSet, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return super(AuthorizationViewSet, self).get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        # print str(type(request))
        request.user = GardenUser.objects.get(username='test1')
        # print request['client_id']
        # print request['redirect_uri']
        return super(AuthorizationViewSet, self).dispatch(request, *args, **kwargs)


# as_view로 구현해보자
class UserOauthViewSet(viewsets.GenericViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    model = GardenUser
    required_scopes = ['read']
    lookup_field = 'username'

    def initial(self, request, *args, **kwargs):
        print request.user
        super(UserOauthViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]


# def me(self, request, *args, **kwargs):
#     print self.get_object()
#     if request.user != self.get_object():
#         return Response(data={"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
#     return Response(data={"전상우": "꺼져"}, status=status.HTTP_200_OK)

# class UserOauthViewSet(viewsets.GenericViewSet,
#                        mixins.RetrieveModelMixin):
#     model = GardenUser
#     serializer_class = UserSerializer
#     authentication_classes = [OAuth2Authentication]
#     permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
#     backend = OAuth2Backend
#     validator_class = OAuth2Validator
#     # oauth2_settings._SCOPES = ['read', 'write', 'scope1', 'scope2']
#     lookup_field = 'username'
#
#     def initial(self, request, *args, **kwargs):
#         super(UserOauthViewSet, self).initial(request, *args, **kwargs)
#         if isinstance(request.DATA, dict):
#             for key in request.DATA.keys():
#                 if type(request.DATA[key]) is list:
#                     request.DATA[key] = request.DATA[key][0]
#
#     @protected_resource()
#     def retrieve(self, request, *args, **kwargs):
#         """
#             Inquiring my Information
#         """
#         user_obj = GardenUser.objects.get_user_obj(kwargs['username'])
#         serializer = UserSerializer(user_obj)
#         serializer.data['profile_img'] = request.user.profile_img.url
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

# class AuthorizationViewSet(AuthorizationView,
#                            viewsets.GenericViewSet,
#                            mixins.ListModelMixin):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = GrantSerializer
#     model = Grant
#
#     # def get_initial(self):
#     #     return super(AuthorizationViewSet, self).get_initial()
#     #
#     # def form_valid(self, form):
#     #     return super(AuthorizationViewSet, self).form_valid(form)
#     #
#     # def get(self, request, *args, **kwargs):
#     #     return super(AuthorizationViewSet, self).get(request, *args, **kwargs)
#
#     def list(self, request, *args, **kwargs):
#         print request.user
#         print "retrieve"
#         # return self.dispatch(request, *args, **kwargs)
#
#     def dispatch(self, request, *args, **kwargs):
#         pass