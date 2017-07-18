from infa_web.apps.restaurante_menus.models import *
from django.db.models import Max
from django.core import serializers
from django.http import HttpResponse

import decimal
import json
from django.views.decorators.csrf import csrf_exempt

def MenuDetailCreate(data,using):
	response = { "data" : [] , "message" : False }

	for key, value in data:
		print value
		plato = Platos.objects.using(using).get(pk=value["cplato"])
		menu = Menus.objects.using(using).get(pk=value["cmenu"])

		if not Menusdeta.objects.using(using).filter(cmenu=menu,cplato=plato).exists():
			it = Menusdeta.objects.using(using).filter(cmenu=menu).aggregate(Max('it'))
			if it["it__max"]:
				it = int(it["it__max"]) + 1
			else:
				it = 1

			value["cmenu"] = menu
			value["cplato"] = plato

			value["it"] = it

			value["vunita"] = plato.vttotal
			value["vtotal"] = float(value["vunita"]) * float(value["canti"])

			menudeta = Menusdeta(**value)

			response["data"].append({
				"DT_RowId": "row_1",
				"detail" : {
					"it" : str(menudeta.it),
					"cplato" : str(menudeta.cplato.cplato),
					"nplato" : str(menudeta.cplato.nplato),
					"canti" : str(menudeta.canti),
					"vunita" : str(menudeta.vunita),
					"vtotal" : str(menudeta.vtotal),
				}
			})

			menudeta.save(using=using)

			menu.vttotal += decimal.Decimal(menudeta.vtotal)
			menu.save(using=using)
		else:
			response["message"] = {"text":"El plato ya se encuentra registrado en el menu","type":"info"}

	response["menu"] = json.loads(serializers.serialize("json", list([menu]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]
	return response

def MenuDetailUpdate(data,using):
	response = { "data" : []  }

	for key, value in data:
		#ingrediente = Ingredientes.objects.using(using).get(pk=value["cingre"])
		plato = Platos.objects.using(using).get(pk=value["cplato"])
		menu = Menus.objects.using(using).get(pk=value["cmenu"])

		value["cmenu"] = menu
		value["cplato"] = plato
		menudeta = Menusdeta.objects.using(using).get(cplato=plato.cplato,cmenu=menu)

		menu.vttotal -= decimal.Decimal(menudeta.vtotal)

		menudeta.canti = float(menudeta.canti)
		menudeta.vunita = float(menudeta.vunita)

		menudeta.vtotal = menudeta.canti * menudeta.vunita

		menudeta.canti = float(value["canti"])
		menudeta.vunita = float(value["vunita"])
		menudeta.vtotal = float(value["canti"]) * float(value["vunita"])

		response["data"].append({
			"DT_RowId": "row_1",
			"detail" : {
				"it" : str(menudeta.it),
				"cplato" : str(menudeta.cplato.cplato),
				"nplato" : str(menudeta.cplato.nplato),
				"canti" : str(menudeta.canti),
				"vunita" : str(menudeta.vunita),
				"vtotal" : str(menudeta.vtotal),
			}
		})

		menudeta.save(using=using)

		menu.vttotal += decimal.Decimal(menudeta.vtotal)
		menu.save(using=using)

	response["menu"] = json.loads(serializers.serialize("json", list([menu]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]

	return response

def MenuDetailRemove(data,using):
	response = { "data" : []  }

	for key, value in data:
		menu = Menus.objects.using(using).get(cmenu=value["cmenu"])
		plato = Platos.objects.using(using).get(pk=value["cplato"])
		menudeta = Menusdeta.objects.using(using).get(cplato=plato,cmenu=menu)

		response["data"].append({})

		menudeta.delete(using=using)

		menu.vttotal -= decimal.Decimal(menudeta.vtotal)
		menu.save(using=using)

	response["menu"] = json.loads(serializers.serialize("json", list([menu]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]

	return response

@csrf_exempt
def GetMenuDetail(request,pk):
	deta = Menusdeta.objects.using(request.db).filter(cmenu=pk)

	data = { "data" :[] }
	for item in deta:
		data["data"].append({
				"DT_RowId": "row_1",
				"detail" : {
					"cplato" : str(item.cplato.cplato),
					"nplato" : str(item.cplato.nplato),
					"it" : str(item.it),
					"canti" : str(item.canti),
					"vunita" : str(item.vunita),
					"vtotal" : str(item.vtotal),
				}
			})
	return HttpResponse(json.dumps(data), content_type="application/json")
