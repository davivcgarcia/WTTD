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
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        Speaker.objects.create(
            name='Davi Garcia',
            slug='davi-garcia',
            url='http://www.davigarcia.com.br',
            description='Passionate software developer!'
        )
        url = r('core:speaker_detail', kwargs={'slug': 'davi-garcia'})
        self.resp = self.client.get(url)

    def test_get(self):
        """
        GET should return 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template should be core/speaker_detail.html.
        """
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        """
        HTML must contain data.
        """
        self.assertContains(self.resp, 'Davi Garcia')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://www.davigarcia.com.br')

    def test_context(self):
        """
        Speaker must be in context.
        """
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    """
    Test class.
    """
    def test_not_found(self):
        """
        Access to a invalid speaker must return 404.
        """
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
