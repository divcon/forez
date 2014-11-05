#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from .serializers import ClientSerializer, ClientCreateSerializer, DetailSerializer, SettingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.renderers import UnicodeJSONRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from .models import GardenClient
from .permissions import ClientPermission
from teams.models import Team


class ClientViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin):
    model = GardenClient
    # model = Client
    serializer_class = ClientSerializer
    queryset = GardenClient.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UnicodeJSONRenderer, )
    permission_checker = ClientPermission()
    lookup_field = 'name'

    def initial(self, request, *args, **kwargs):
        super(ClientViewSet, self).initial(request, *args, **kwargs)
        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def get_queryset(self):
        client_set = self.queryset.filter(user=self.request.user)

        return client_set

    def create(self, request, *args, **kwargs):
        """
            Registering client(app)
        """
        serializer = ClientCreateSerializer(data=request.DATA, context={'request': request})
        if serializer.is_valid():
            # create should be in serializers.py
            created_client = GardenClient.objects.create(
                user=request.user,
                name=serializer.data['name'],
                url=serializer.data['url'],
                redirect_uri=serializer.data['redirect_uri'],
                client_type=serializer.data['client_type'],
                #delete client_name or display_name
                client_name=serializer.data['name'],
                display_name=serializer.data['name'],
                contact_email=request.user.email)
            created_team = Team.objects.create(
                member=request.user,
                client=created_client,
                is_owner=True, )

            response_data = {"client_id": created_client.client_id,
                             "client_secret": created_client.client_secret,
                             "client_type": created_client.client_type,
                             #app name
                             "client_name": created_client.name,
                             "team_owner": created_team.member.username, }
            return Response(response_data, status.HTTP_201_CREATED)

        else:
            return Response(data={'error': 'Application name is already exist'}, status=status.HTTP_409_CONFLICT)
            # return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """
            Listing clients(apps)
        """
        clients_list = Team.objects.all().filter(member=request.user.username)
        result_list = list()
        for c in clients_list:
            tmp_dict = dict()
            tmp_dict['name'] = c.client.name
            tmp_dict['owner'] = Team.objects.get_team_owner(c.client).member.username
            result_list.append(tmp_dict)
        # return super(ClientViewSet, self).list(request, *args, **kwargs)
        return Response(data=result_list, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
            Searching client(app) by using application name
        """
        # if request.user != self.get_object().user:
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        client_name = kwargs['name']
        if not self.permission_checker.has_permission(request, client_name):
            return Response(data={"error": "no authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
        client_obj = GardenClient.objects.get_client_obj(client_name)
        serializer = ClientSerializer(client_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return super(ClientViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
            modifying Client URL
        """
        client_name = kwargs['name']
        if not self.permission_checker.has_permission(request, client_name=client_name):
            return Response(data={"error": "no authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
        url = request.DATA['url']
        redirect_uri = request.DATA['redirect_uri']

        client_obj = GardenClient.objects.get_client_obj(client_name)
        client_obj.url = url
        client_obj.redirect_uri = redirect_uri
        client_obj.save(update_fields=['url', 'redirect_uri'])
        return Response(data=request.DATA, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
            Unregistering client(app)
        """
        if request.user != self.get_object().user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super(ClientViewSet, self).destroy(request, *args, **kwargs)

    @action(['POST', 'GET'])
    def details(self, request, name=None):
        if not self.permission_checker.has_permission(request, name):
            return Response(data={"error": "no authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        client_obj = GardenClient.objects.get_client_obj(name)
        if request.method == 'GET':
            serializer = DetailSerializer(client_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            client_obj.tag1 = request.DATA['tag1']
            client_obj.tag2 = request.DATA['tag2']
            client_obj.tag3 = request.DATA['tag3']
            client_obj.category = request.DATA['category']
            client_obj.short_description = request.DATA['short_description']
            client_obj.long_description = request.DATA['long_description']
            client_obj.permission_explanation = request.DATA['permission_explanation']
            client_obj.save(update_fields=['tag1', 'tag2', 'tag3', 'category', 'short_description',
                                           'long_description', 'permission_explanation'])
            return Response(data=request.DATA, status=status.HTTP_200_OK)

    @action(['POST', 'GET'])
    def setting(self, request, name=None):
        if not self.permission_checker.has_permission(request, name):
            return Response(data={"error": "no authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        client_obj = GardenClient.objects.get_client_obj(name)
        if request.method == 'GET':
            serializer = SettingSerializer(client_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            client_obj.display_name = request.DATA['display_name']
            client_obj.contact_email = request.DATA['contact_email']
            client_obj.publish = request.DATA['publish']
            if (request.DATA['publish'] == 'true') or (request.DATA['publish'] == 'True'):
                client_obj.publish = True
            elif (request.DATA['publish'] == 'false') or (request.DATA['publish'] == 'False'):
                client_obj.publish = False
                print client_obj.publish
            else:
                return Response(data={"error": "Attribute error. Check your request body"},
                                status=status.HTTP_400_BAD_REQUEST)
            client_obj.save(update_fields=['display_name', 'contact_email', 'publish'])
            return Response(data=request.DATA, status=status.HTTP_200_OK)

    @action(['GET'])
    def logs(self, request, name=None):
        if request.method == 'GET':
            pass