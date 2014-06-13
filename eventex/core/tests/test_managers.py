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
from eventex.core.models import Speaker, Contact


class ContactManagerTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        s = Speaker.objects.create(
            name='Davi Garcia',
            slug='davi-garcia',
            url='http://www.davigarcia.com.br'
        )
        s.contact_set.add(
            Contact(kind='E', value='davivcgarcia@gmail.com'),
            Contact(kind='P', value='21-98765432'),
            Contact(kind='F', value='21-12345678')
        )

    def test_emails(self):
        """
        Manager should provide email queryset.
        """
        qs = Contact.emails.all()
        expected = ['<Contact: davivcgarcia@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phone(self):
        """
        Manager should provide email queryset.
        """
        qs = Contact.phones.all()
        expected = ['<Contact: 21-98765432>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        """
        Manager should provide email queryset.
        """
        qs = Contact.faxes.all()
        expected = ['<Contact: 21-12345678>']
        self.assertQuerysetEqual(qs, expected)
