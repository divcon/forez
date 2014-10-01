#-*- coding: utf-8 -*-
from .serializers import ClientSerializer
from provider.oauth2.models import Client
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.renderers import UnicodeJSONRenderer
from rest_framework.authentication import TokenAuthentication
from users.models import GardenUser


class ClientCreateViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin):
    model = Client
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UnicodeJSONRenderer, )

    def initial(self, request, *args, **kwargs):
        super(ClientCreateViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def get_queryset(self):
        client_set = self.queryset.filter(user=self.request.user)

        return client_set

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.DATA, context={'request': request})
        if serializer.is_valid():
            if self.queryset.filter(user=request.user, name=serializer.data['name']):
                data = {"duplicated": "client name is duplicated"}
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

            # create should be in serializers.py
            created_client = Client.objects.create(
                user=request.user,
                name=serializer.data['name'],
                url=serializer.data['url'],
                redirect_uri=serializer.data['redirect_uri'],
                client_type=serializer.data['client_type'],)

            response_data = {"client_id": created_client.client_id,
                             "client_secret": created_client.client_secret,
                             "client_type": created_client.client_type, }
            return Response(response_data, status.HTTP_201_CREATED)

        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class ClientViewSet(viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin):
    model = Client
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UnicodeJSONRenderer, )
    lookup_field = 'user'

    def initial(self, request, *args, **kwargs):
        super(ClientViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def retrieve(self, request, *args, **kwargs):
        # if request.user != self.get_object():
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        return super(ClientViewSet, self).retrieve(request, *args, **kwargs)