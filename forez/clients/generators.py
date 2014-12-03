#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from oauth2_provider.generators import BaseHashGenerator
from oauthlib.common import generate_client_id as oauthlib_generate_client_id
from forez import settings


CLIENT_ID_CHARACTER_SET = r'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


class GardenClientIdGenerator(BaseHashGenerator):
    def hash(self):
        client_id_charset = CLIENT_ID_CHARACTER_SET.replace(":", "")
        return oauthlib_generate_client_id(length=40, chars=client_id_charset)


class ClientSecretGenerator(BaseHashGenerator):
    def hash(self):
        return oauthlib_generate_client_id(length=128, chars=CLIENT_ID_CHARACTER_SET)
