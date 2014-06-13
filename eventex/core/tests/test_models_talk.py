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
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time=u'10:00'
        )

    def test_create(self):
        """
        Talk object must be saved to db.
        """
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        """
        Talk object must have unicode format.
        """
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_speakers(self):
        """
        Talk has many Speakers and vice-versa.
        """
        self.talk.speakers.create(
            name='Davi Garcia',
            slug='davi-garcia',
            url='http://www.davigarcia.com.br'
        )
        self.assertEqual(1, self.talk.speakers.count())
