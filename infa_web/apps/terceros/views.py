from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from django import forms

from infa_web.apps.terceros.forms import *


# thirdParty #
class ThirdPartyCreate(CreateView):
	model = Tercero
	template_name = "terceros/third-party.html"
	form_class = ThirdPartyForm
	success_url=reverse_lazy("add-third-party")
	
class ThirdPartyUpdate(UpdateView):
	model = Tercero
	template_name = "terceros/third-party.html"
	success_url=reverse_lazy("add-third-party")
	form_class = ThirdPartyForm

class ThirdPartyList(ListView):
	model = Tercero
	template_name = "terceros/list-third-parties.html"
# thirdParty #
