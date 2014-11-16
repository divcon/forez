
from rest_framework import serializers
from oauth2_provider.models import Grant


class GrantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Grant
        fields = ('user', 'code', 'application', 'redirect_uri')
        lookup_field = 'client'















# user = models.ForeignKey(AUTH_USER_MODEL)
#     code = models.CharField(max_length=255, db_index=True)  # code comes from oauthlib
#     application = models.ForeignKey(oauth2_settings.APPLICATION_MODEL)
#     expires = models.DateTimeField()
#     redirect_uri = models.CharField(max_length=255)
#     scope = models.TextField(blank=True)