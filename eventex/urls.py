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
DATE: 05/20/2014
"""

from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
	# View created on first day of class (May 18th, 2014).
    url(r'^$', 'eventex.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
