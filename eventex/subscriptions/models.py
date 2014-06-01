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
DATE: 05/29/2014
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
	name = models.CharField(_('nome'), max_length=100)
	cpf = models.CharField(_('CPF'), max_length=11, unique=True)
	email = models.EmailField(_('email'), unique=True)
	phone = models.CharField(_('telefone'), max_length=20, blank=True)
	created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

	class Meta:
		ordering = ['created_at']
		verbose_name = _(u'inscrição')
		verbose_name_plural = _(u'inscrições')

	def __unicode__(self):
		return self.name
	
		