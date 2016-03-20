# -*- coding: utf-8 -*-
# @Author: YungLeChao
# @Date:   2016-03-20 10:42:05
# @Last Modified by:   YungLeChao
# @Last Modified time: 2016-03-20 11:34:23
from django.contrib.auth import get_user_model, SESSION_KEY
from django.test import TestCase
from unittest.mock import patch
User = get_user_model()


class LoginViewTest(TestCase):

    @patch('accounts.views.authenticate')
    def test_call_authenticate_with_assertion_from_post(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'assert this'})
        mock_authenticate.assert_called_once_with(
            assertion='assert this')

    @patch('accounts.views.authenticate')
    def test_gets_logged_in_session_if_authenticate_returns_a_user(self, mock_authenticate):
        user = User.objects.create(email='a@b.com')
        user.backend = ''
        mock_authenticate.return_value = user
        self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertEqual(self.client.session[SESSION_KEY], user.pk)

    @patch('accounts.views.authenticate')
    def test_does_not_get_logged_in_session_if_authenticate_returns_None(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post('/accounts/login', {'assertion': 'a'})
        self.assertNotIn(SESSION_KEY, self.client.session)
