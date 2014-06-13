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


class KindContactManager(models.Manager):
    """
    Generic RelatedManager for contact.
    """
    def __init__(self, kind):
        """
        Class constructor.
        """
        super(KindContactManager, self).__init__()
        self.kind = kind

    def get_queryset(self):
        """
        Define custom queryset for contact kind.
        """
        qs = super(KindContactManager,self).get_queryset()
        qs = qs.filter(kind=self.kind)
        return qs
