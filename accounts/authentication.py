# -*- coding: utf-8 -*-
# @Author: YungLeChao
# @Date:   2016-03-20 11:45:45
# @Last Modified by:   YungLeChao
# @Last Modified time: 2016-03-20 15:04:35
import requests

from django.contrib.auth import get_user_model

User = get_user_model()
PERSONA_VERIFY_URL = 'https://verifier.persona.org/verify'
DOMAIN = 'localhost'


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': DOMAIN}
        )
        if response.ok and response.json()['status'] == 'okay':
            email = response.json()['email']
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return User.objects.create(email=email)

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
