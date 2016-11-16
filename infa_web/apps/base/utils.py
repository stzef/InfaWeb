from django.core.exceptions import ObjectDoesNotExist

def get_or_none(Model, db, **kwargs):
	try:
		return Model.objects.using(db).get(**kwargs)
	except ObjectDoesNotExist:
		return None

def get_list_or_none(Model, db, **kwargs):
	obj_list = list(Model.objects.using(db).filter(**kwargs))
	if not obj_list:
		return None
	return obj_list
