from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth import login as auth_login

class loginView(FormView):
	template_name = 'usuarios/login.html'
	success_url = '/'
	form_class = loginForm

	def get_context_data(self, **kwargs):
		context = super(loginView, self).get_context_data(**kwargs)
		context['domain'] = self.request.subdomain
		return context

	def form_valid(self, form):
		response = form.auth_user(request_bd = self.request.db)
		if response is not None:
			auth_login(self.request, response)
			return HttpResponseRedirect('/')
		else:
			return self.form_invalid(form)
		return super(loginView, self).form_valid(form)