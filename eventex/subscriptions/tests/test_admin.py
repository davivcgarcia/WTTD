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

from django.test import TestCase
from mock import Mock
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin

class MarkAsPaidTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Creates an instance of Model Admin.
        """
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(
            name='Davi Garcia',
            cpf='12345678901',
            email='davigarcia@gmail.com',
            phone='(21) 1234-5678'
        )

    def test_has_action(self):
        """
        Action is installed.
        """
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """
        Action to mark all selected as paid.
        """
        fake_request = Mock()
        queryset =  Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
