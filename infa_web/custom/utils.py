from infa_web.config.domaindb import DOMAINS
from infa_web.apps.base.models import *


def get_subdomain_by_name_db(name_db):
	domain = ""
	for nempresa, ndb in DOMAINS.iteritems():
		if ndb == name_db:
			domain =nempresa
	return domain

def get_choices_timo(using,query={}):
	query["prefijo"] = ""
	options_group = Timo.objects.using(using).filter(**query)
	choices = []
	for option_group in options_group:
		choice = []
		list_group = Timo.objects.using(using).filter(ctimo__startswith=option_group.ctimo).exclude(ctimo=option_group.ctimo)
		choice.append(option_group.ntimo)
		list_ = []
		for option in list_group:
			list_.append((option.pk,option.ntimo))
		choice.append(tuple(list_))
		choices.append(tuple(choice))
	#print tuple(choices)
	return tuple(choices)

def get_choices_tifopa(using,query={}):
	query["ctifopa__in"] = [1,2]
	options_group = Tifopa.objects.using(using).filter(**query)
	choices = []
	for option_group in options_group:
		choice = []
		list_group = Tifopa.objects.using(using).filter(ctifopa__startswith=option_group.ctifopa).exclude(ctifopa=option_group.ctifopa)
		choice.append(option_group.ntifopa)
		list_ = []
		for option in list_group:
			list_.append((option.pk,option.ntifopa))
		choice.append(tuple(list_))
		choices.append(tuple(choice))
	#print tuple(choices)
	return tuple(choices)
