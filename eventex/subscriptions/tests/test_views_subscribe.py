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
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        """
        GET /inscricao/ must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Response should be a rendered template.
        """
        self.assertTemplateUsed(
            self.resp,
            'subscriptions/subscription_form.html'
        )

    def test_html(self):
        """
        HTML must contain form input controls and tags.
        """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """
        HTML must contain csrf token.
        """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        Context must have the subscription form.
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        data = dict(
            name='Davi Garcia',
            cpf='12345678901',
            email='davivcgarcia@gmail.com',
            phone='21-12345678'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        """
        Valid POST should redirect to /inscricao/1.
        """
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        """
        Valid POST must be saved.
        """
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        data = dict(
            name='Davi Garcia',
            cpf='123456789012',
            email='davivcgarcia@gmail.com',
            phone='21-12345678'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        """
        Invalid POST should not be redirect.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        """
        Form must contain errors.
        """
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        """
        Invalid POST should not save data.
        """
        self.assertFalse(Subscription.objects.exists())

class TemplateRegressionTest(TestCase):
    """
    Regression test class.
    """
    def test_template_has_non_field_errors(self):
        """
        Check if non_field_errors are shown in template.
        """
        invalid_data = dict(name='Henrique Bastos', cpf='12345678901')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)
        self.assertContains(response, '<ul class="errorlist">')