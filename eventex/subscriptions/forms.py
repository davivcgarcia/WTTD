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

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription

def CPFValidator(value):
    """
    Custom validator for CPF field.
    """
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    elif len(value) != 11:
        raise ValidationError(_(u'CPF deve conter 11 números'))

class SubscriptionForm(forms.ModelForm):
    """
    Class to map the form used for Subscriptions app.
    """

    class Meta(object):
        """
        Meta-class to bind this form to model Subscription.
        """
        model = Subscription
        exclude = ('paid',)
        # fields = ('name', 'cpf', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        """
        Constructor appending the new validator for CPF.
        """
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].validators.append(CPFValidator)
