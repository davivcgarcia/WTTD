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
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        self.speaker = Speaker(
            name='Davi Garcia',
            slug='davi-garcia',
            url='http://www.davigarcia.com.br',
            description='Passionate software developer!'
        )
        self.speaker.save()

    def test_create(self):
        """
        Speaker instance must be saved.
        """
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        """
        Speaker string representation should be the name.
        """
        self.assertEqual(u'Davi Garcia', unicode(self.speaker))


class ContactModelTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        self.speaker = Speaker.objects.create(
            name='Davi Garcia',
            slug='davi-garcia',
            url='http://www.davigarcia.com.br',
            description='Passionate software developer!'
        )

    def test_email(self):
        """
        Speaker should have email contact.
        """
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='henrique@bastos.net'
        )
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        """
        Speaker should have email contact.
        """
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='P',
            value='21-987654321'
        )
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        """
        Speaker should have email contact.
        """
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='F',
            value='21-123456789'
        )
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        """
        Contact kind must be limited to E, P or F.
        """
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        """
        Contact string representation should be value.
        """
        contact = Contact(
            speaker=self.speaker,
            kind='E',
            value='davivcgarcia@gmail.com')
        self.assertEqual(u'davivcgarcia@gmail.com', unicode(contact))
