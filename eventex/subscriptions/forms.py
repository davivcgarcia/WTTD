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
from django.core.validators import EMPTY_VALUES
from eventex.subscriptions.models import Subscription


def CPFValidator(value):
    """
    Custom validator for CPF field.
    """
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    elif len(value) != 11:
        raise ValidationError(_(u'CPF deve conter 11 números'))


class PhoneWidget(forms.MultiWidget):
    """
    Widget to have another HTML input field for DDD.
    """
    def __init__(self, attrs=None):
        """
        Class constructor.
        """
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs)
        )
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField()
        )
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return ''
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'DDD inválido.'))
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'Número inválido.'))
        return '%s-%s' % tuple(data_list)


class SubscriptionForm(forms.ModelForm):
    """
    Class to map the form used for Subscriptions app.
    """
    phone = PhoneField(label=_('Telefone'), required=False)
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

    def clean_name(self):
        """
        Function to extend name field validation.
        """
        name = self.cleaned_data['name']
        list_words = name.split()
        capitalized_name = []
        for word in list_words:
            if len(word) == 2:
                capitalized_name.append(word.lower())
            else:
                capitalized_name.append(word.capitalize())
        return ' '.join(capitalized_name)

    def clean(self):
        """
        """
        super(SubscriptionForm, self).clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError(_('Precisa informar seu e-mail ou telefone'))
        
        return self.cleaned_data
