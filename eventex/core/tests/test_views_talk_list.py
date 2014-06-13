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
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk


class TalkListTest(TestCase):
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
            url='http://www.davigarcia.com.br',
            description='Passionate software developer!'
        )
        t1 = Talk.objects.create(
            description='Descrição da palestra.',
            title='Título da palestra.',
            start_time='10:00'
        )
        t2 = Talk.objects.create(
            description='Descrição da palestra.',
            title='Título da palestra.',
            start_time='13:00'
        )
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        """
        GET must return 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template should be core/talk_list.html.
        """
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        """
        HTML should list talks.
        """
        self.assertContains(self.resp, 'Título da palestra', 2)
        self.assertContains(self.resp, '10:00')
        self.assertContains(self.resp, '13:00')
        self.assertContains(self.resp, '/palestras/1/')
        self.assertContains(self.resp, '/palestras/2/')
        self.assertContains(self.resp, '/palestrantes/davi-garcia/', 2)
        self.assertContains(self.resp, 'Passionate software developer!', 2)
        self.assertContains(self.resp, 'Davi Garcia', 2)
        self.assertContains(self.resp, 'Descrição da palestra', 2)

    def test_morning_talk_in_context(self):
        """
        Context must have 'morning_talks' list.
        """
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talk_in_context(self):
        """
        Context must have 'afternoon_talk' list.
        """
        self.assertIn('afternoon_talks', self.resp.context)
