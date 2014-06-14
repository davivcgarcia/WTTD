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
from django.template import Template, Context


class YoutubeTagTest(TestCase):
    """
    Test class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        context = Context({'ID': 1})
        template = Template('{% load youtube %}{% youtube ID %}')
        self.content = template.render(context)

    def test_output(self):
        """
        Tag must be rendered by template.
        """
        self.assertIn('<object', self.content)
        self.assertIn('/1', self.content)
