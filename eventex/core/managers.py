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

from django.db import models


class EmailContactManager(models.Manager):
    """
    RelatedManager class for emails on contact.
    """
    def get_queryset(self):
        """
        Define custom queryset.
        """
        qs = super(EmailContactManager, self).get_queryset()
        qs = qs.filter(kind='E')
        return qs


class PhoneContactManager(models.Manager):
    """
    RelatedManager class for phones on contacts.
    """
    def get_queryset(self):
        """
        Define custom queryset.
        """
        qs = super(PhoneContactManager, self).get_queryset()
        qs = qs.filter(kind='P')
        return qs


class FaxContactManager(models.Manager):
    """
    RelatedManager class for phones on contacts.
    """
    def get_queryset(self):
        """
        Define custom queryset.
        """
        qs = super(FaxContactManager, self).get_queryset()
        qs = qs.filter(kind='F')
        return qs
