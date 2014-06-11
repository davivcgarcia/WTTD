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
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    """
    Test Class.
    """
    def test_form_has_fields(self):
        """
        Form must have 4 fields.
        """
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        """
        CPF must only accept digits.
        """
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        """
        CPF must have 11 digits.
        """
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        """
        Email is optional.
        """
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_name_must_be_capitalized(self):
        """
        Name must be capitalized.
        """
        form = self.make_validated_form(name='DaVi DA sILva')
        self.assertEqual('Davi da Silva', form.cleaned_data['name'])

    def test_must_inform_email_or_phone(self):
        """
        Make sure that email or phone are populated.
        """
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        """
        Creates a valid form and changes it based on kwargs.
        """
        data = dict(
            name='Davi Garcia',
            cpf='12345678901',
            email='davigarcia@gmail.com',
            phone_0='21',
            phone_1='12345678'
        )
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
