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
from eventex.core.managers import KindContactManager, PeriodManager


class Speaker(models.Model):
    """
    DB Model to store detail information of speakers.
    """
    name = models.CharField(_(u'Nome'), max_length=255)
    slug = models.SlugField(_(u'Slug'))
    url = models.URLField(_(u'Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    class Meta(object):
        verbose_name = _(u'palestrante')
        verbose_name_plural = _(u'palestrantes')

    def __unicode__(self):
        """
        Unicode representation of the object.
        """
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})


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


class Talk(models.Model):
    """
    DB Model to store detail information of talks.
    """
    title = models.CharField(_(u'Título'), max_length=200)
    description = models.TextField(_(u'Descrição'))
    start_time = models.TimeField(_(u'Horário'), blank=True)
    speakers = models.ManyToManyField(u'Speaker', verbose_name=_(u'palestrantes'))

    objects = PeriodManager()

    class Meta(object):
        verbose_name = _(u'palestra')
        verbose_name_plural = _(u'palestras')

    def __unicode__(self):
        """
        Unicode representation of the object.
        """
        return self.title

    def get_absolute_url(self):
        # TODO: Use Reverse.
        return '/palestras/%d/' % self.pk
