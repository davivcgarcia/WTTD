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
from eventex.core.models import Speaker, Contact


class ContactInline(admin.TabularInline):
    """
    Class used to define display inline Speaker's contact.
    """
    model = Contact
    extra = 1


class SpeakerAdmin(admin.ModelAdmin):
    """
    Class used to define display settings for Speaker's admin page.
    """
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Speaker, SpeakerAdmin)
