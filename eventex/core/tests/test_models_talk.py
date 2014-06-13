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
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager


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

    def test_period_manager(self):
        """
        Talk default manager must be instance of PeriodManager.
        """
        self.assertIsInstance(Talk.objects, PeriodManager)


class CourseModelTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        self.course = Course.objects.create(
            title=u'Tutorial Django',
            description=u'Descrição do curso.',
            start_time=u'10:00',
            slots=20
        )

    def test_create(self):
        """
        Course object must be saved to db.
        """
        self.assertEqual(1, self.course.pk)

    def test_unicode(self):
        """
        Course object must have custom unicode representation.
        """
        self.assertEqual(u'Tutorial Django', unicode(self.course))

    def test_speaker(self):
        """
        Course have many speakers and vice-versa.
        """
        self.course.speakers.create(
            name='Davi Garcia',
            slug='davi-garcia',
            url='http://www.davigarcia.com.br'
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_period_manager(self):
        """
        Course default manager must be instance of Period Manager.
        """
        self.assertIsInstance(Course.objects, PeriodManager)


class PeriodManagerTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        Talk.objects.create(
            title='Morning Talk', start_time='10:00'
        )
        Talk.objects.create(
            title='Afternoon Talk', start_time='13:00'
        )

    def test_morning(self):
        """
        Should return only talks before 12:00.
        """
        self.assertQuerysetEqual(
            Talk.objects.at_morning(),
            ['Morning Talk'],
            lambda t: t.title
        )

    def test_afternoon(self):
        """
        Should return only talks after 11:59:59.
        """
        self.assertQuerysetEqual(
            Talk.objects.at_afternoon(),
            ['Afternoon Talk'],
            lambda t: t.title
        )
