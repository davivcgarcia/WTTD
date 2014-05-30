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

AUTHOR: Davi Garcia (davivcgarcia@gmail.com)
DATE: 05/29/2014
"""

from django.test import TestCase

class HomeTest(TestCase):

	def setUp(self):
		"""
		Test initialization.
		"""
		self.resp = self.client.get('/')

	def test_get(self):
		"""
		GET / must return status code 200.
		"""
		self.assertEqual(200,self.resp.status_code)
	
	def test_template(self):
		"""
		Home view must use template index.html.
		"""
		self.assertTemplateUsed(self.resp,'index.html')
