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
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager


class Speaker(models.Model):
    """
    DB Model to store detail information of speakers.
    """
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_('Descrição'), blank=True)

    def __unicode__(self):
        """
        Unicode representation of the object.
        """
        return self.name


class Contact(models.Model):
    """
    DB Model to store contact information of speakers.
    """
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax'))
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager(kind='E')
    phones = KindContactManager(kind='P')
    faxes = KindContactManager(kind='F')

    def __unicode__(self):
        """
        Unicode representation of the object.
        """
        return self.value
