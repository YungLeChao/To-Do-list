# -*- coding: utf-8 -*-
# @Author: YungLeChao
# @Date:   2016-03-20 13:46:10
# @Last Modified by:   YungLeChao
# @Last Modified time: 2016-03-20 13:50:47
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):

    def test_user_is_valid_with_email(self):
        user = User(email='a@b.com')
        user.full_clean()

    def test_email_is_primary_key(self):
        user = User()
        self.assertFalse(hasattr(user, 'id'))

    def test_is_authenticated(self):
        user = User()
        self.assertTrue(user.is_authenticated())
