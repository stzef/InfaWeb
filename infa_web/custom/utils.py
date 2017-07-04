from infa_web.config.domaindb import DOMAINS
from infa_web.apps.base.models import *

from django.contrib.auth.models import Permission

from django.db.models import Q

def get_subdomain_by_name_db(name_db):
	domain = ""
	for nempresa, ndb in DOMAINS.iteritems():
		if ndb == name_db:
			domain =nempresa
	return domain

def get_user_permissions(user,db):
	# Retorna los permisos (object db) de un usuarios
	if user.is_superuser:
		return Permission.objects.using(db).all()
	return user.user_permissions.all() | Permission.objects.using(db).filter(group__user=user)

def get_nav_submenu(id,permissions,db):
	menu = NavMenus.objects.using(db).get(pk=id)

	#menus = NavMenus.objects.using(db).filter(father=menu,permission__in=permissions)
	modules_enabled = Modules.objects.using(db).filter(enabled=True,enabled_enterprise=True)
	menus = NavMenus.objects.using(db).filter(father=menu).filter(module__in=modules_enabled).filter(Q(permission__in=permissions) | Q(permission=None)).order_by('orden')
	for submenu in menus:
		submenu.submenus = get_nav_submenu(submenu.id,permissions,db)

	return menus

def get_nav_menu(permissions,db):
	#menus = NavMenus.objects.using(db).filter(main=True,permission__in=permissions)
	modules_enabled = Modules.objects.using(db).filter(enabled=True,enabled_enterprise=True)
	menus = NavMenus.objects.using(db).filter(main=True).filter(module__in=modules_enabled).filter(Q(permission__in=permissions) | Q(permission=None)).order_by('orden')

	for menu in menus:
		menu.submenus = get_nav_submenu(menu.id,permissions,db)

	return menus

def get_quick_access(permissions,db):
	modules_enabled = Modules.objects.using(db).filter(enabled=True,enabled_enterprise=True)
	quick_access = NavMenus.objects.using(db).filter(quick_access=True).filter(module__in=modules_enabled).filter(Q(permission__in=permissions) | Q(permission=None)).order_by('orden')
	return quick_access

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
