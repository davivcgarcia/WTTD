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

from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    """
    Class used to define display settings for model's admin page.
    """
    list_display = (
        'name', 'email', 'cpf', 'phone', 'created_at',
        'subscribed_today', 'paid',
    )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email','cpf', 'phone', 'created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        """
        Function to create a custom column that confirms if the
        person subscribed at the same day as checked (today).
        """
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)
