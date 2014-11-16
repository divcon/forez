#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from oauth2_provider.views.base import AuthorizationView, TokenView
from users.models import GardenUser


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


class TokenViewSet(TokenView):
    pass

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