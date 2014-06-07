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

from datetime import datetime
from django.test import TestCase
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        self.obj = Subscription(
            name='Davi Garcia',
            cpf='12345678901',
            email='davigarcia@gmail.com',
            phone='(21) 1234-5678'
        )

    def test_create(self):
        """
        Subscription must have name, cpf, email, phone.
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """
        Subscriptions must have automatic create_at.
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        """
        Verify the unicode representation of the object.
        """
        self.assertEqual(u'Davi Garcia', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        """
        Verfy if the default value for paid is False.
        """
        self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        Subscription.objects.create(
            name='Davi Garcia',
            cpf='12345678901',
            email='davigarcia@gmail.com',
            phone='(21) 1234-5678'
        )

    def test_cpf_unique(self):
        """
        CPF must be unique.
        """
        sub = Subscription(
            name='David Garcia',
            cpf='12345678901',
            email='davigarcia@yahoo.com',
            phone='(21) 4321-5678'
        )
        self.assertRaises(IntegrityError, sub.save)

    def test_email_can_repeat(self):
        """
        CPF don't need to be unique.
        """
        sub = Subscription.objects.create(
            name='David Garcia',
            cpf='10987654321',
            email='davigarcia@gmail.com',
            phone='(21) 4321-5678'
        )
        self.assertEqual(2, sub.pk)
