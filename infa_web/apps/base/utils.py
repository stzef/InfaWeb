from django.core.exceptions import ObjectDoesNotExist

def get_or_none(Model, db, **kwargs):
	try:
		return Model.objects.using(db).get(**kwargs)
	except ObjectDoesNotExist:
		return None