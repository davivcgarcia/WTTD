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
DATE: 05/30/2014
"""

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
    """
    Test Class.
    """
    def setUp(self):
        """
        Test initialization.
        """
        sub = Subscription.objects.create(name='Davi Garcia',
                                          cpf='12345678901',
                                          email='davivcgarcia@gmail.com',
                                          phone='21-12345678')
        self.resp = self.client.get('/inscricao/%d/' % sub.pk)

    def test_get(self):
        """
        GET /inscricao/1/ must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Response should be a rendered template.
        """
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        """
        Context must have a subscription instance.
        """
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        """
        Check if subscription data was rendered.
        """
        self.assertContains(self.resp, 'Em breve, entraremos em contato')

class DetailNotFound(TestCase):
    """
    Test Class.
    """
    def test_not_found(self):
        """
        Verify if the HTTP/404 will return in case of invalid subscription.
        """
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
