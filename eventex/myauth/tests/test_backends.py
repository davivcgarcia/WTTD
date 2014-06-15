# coding: utf-8
"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from unittest import skip
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.auth import get_user_model
from eventex.myauth.backends import EmailBackend


@skip
class EmailBackendTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='davi',
            email='davivcgarcia@gmail.com',
            password='abracadabra'
        )
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        """
        Backend should be able to handle email as user id.
        """
        user = self.backend.authenticate(
            email='davivcgarcia@gmail.com',
            password='abracadabra'
        )
        self.assertIsNotNone(user)

    def test_wrong_password(self):
        """
        Backend should not authenticate user with bad password.
        """
        user = self.backend.authenticate(
            email='davivcgarcia@gmail.com',
            password='wrong'
        )
        self.assertIsNone(user)

    def test_unknown_user(self):
        """
        Backend should not authenticate unknown user.
        """
        user = self.backend.authenticate(
            email='unknown@gmail.com',
            password='wrong'
        )
        self.assertIsNone(user)

    def test_get_user(self):
        """
        Backend should have 'get_user' method.
        """
        self.assertIsNotNone(self.backend.get_user(1))


@skip
class MultipleEmailsTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='user1',
            email='davivcgarcia@gmail.com',
            password='abracadabra',
        )
        UserModel.objects.create_user(
            username='user2',
            email='davivcgarcia@gmail.com',
            password='abracadabra',
        )
        self.backend = EmailBackend()

    def test_multiple_emails(self):
        """
        Backend should not authenticate users with same emails.
        """
        user = self.backend.authenticate(
            email='davivcgarcia@gmail.com',
            password='abracadabra'
        )
        self.assertIsNone(user)


@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username='davi',
            email='davivcgarcia@gmail.com',
            password='abracadabra'
        )

    def test_login_with_email(self):
        """
        Backend should be able to authenticate based on email as email.
        """
        result = self.client.login(
            email='davivcgarcia@gmail.com',
            password='abracadabra'
        )
        self.assertTrue(result)

    def test_login_with_username(self):
        """
        Backend should be able to authenticate based on email as username.
        """
        result = self.client.login(
            username='davivcgarcia@gmail.com',
            password='abracadabra'
        )
        self.assertTrue(result)
