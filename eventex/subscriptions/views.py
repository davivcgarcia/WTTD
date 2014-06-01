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

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.forms import SubscriptionForm

def subscribe(request):
	"""
	Handler to dispatch the correct view to each method.
	"""
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	"""
	New accesses need to see the form in clean state.
	"""
	return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})

def create(request):
	"""
	Requests with POST data need to be handled as creation.
	"""
	form = SubscriptionForm(request.POST)
	if form.is_valid():
		obj = form.save()
		return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
	else:
		return render(request, 'subscriptions/subscription_form.html', {'form': form})

def detail(request, pk):
	"""
	Access the detail page should handle a specific subscription.
	"""
	subscription = get_object_or_404(Subscription, pk=pk)
	return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})
	