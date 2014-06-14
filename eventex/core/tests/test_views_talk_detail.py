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
from eventex.core.models import Talk


class TalkDetailTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(name='Davi Garcia', slug='davi-garcia')
        self.resp = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        """
        GET must return 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        View must render template 'core/talk_detail.html'.
        """
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_context(self):
        """
        HTTP Response must have template context.
        """
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        """
        GET to a invalid talk URL must return 404.
        """
        response = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, response.status_code)

    def test_html(self):
        """
        HTML must have the structures.
        """
        self.assertContains(self.resp, 'Talk')
        self.assertContains(self.resp, '/palestrantes/davi-garcia/')
        self.assertContains(self.resp, 'Davi Garcia')
