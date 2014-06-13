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

from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk


def home(request):
    """
    View to render the home page.
    """
    return render(request, 'index.html')


def speaker_detail(request, slug):
    """
    View to render the speaker detail page.
    """
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(
        request,
        'core/speaker_detail.html',
        context
    )


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon()
    }
    return render(request, 'core/talk_list.html', context)
