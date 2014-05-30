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
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
	def test_form_has_fields(self):
		"""
		Form must have 4 fields.
		"""
		form = SubscriptionForm()
		self.assertItemsEqual(['name','email','cpf', 'phone'], form.fields)