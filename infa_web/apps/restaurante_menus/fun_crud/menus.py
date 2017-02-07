from infa_web.apps.restaurante_menus.models import *
from django.db.models import Max
from django.core import serializers
from django.http import HttpResponse


import decimal
import json
from django.views.decorators.csrf import csrf_exempt



def MenuDetailCreate(data,using):
	response = { "data" : []  }

	for key, value in data:
		plato = Platos.objects.using(using).get(pk=value["platos"]["cplato"])
		menu = Menu.objects.using(using).get(pk=value["platos"]["cmenu"])

		if not Menusdeta.objects.using(using).filter(cmenu=menu,cplato=plato).exists():
			it = Menusdeta.objects.using(using).filter(cmenu=menu).aggregate(Max('it'))
			if it["it__max"]:
				it = int(it["it__max"]) + 1
			else:
				it = 1


			value["platos"]["cmenu"] = menu
			value["platos"]["cplato"] = plato

			value["platos"]["it"] = it

			value["platos"]["vunita"] = plato.vcosto
			value["platos"]["vtotal"] = float(value["platos"]["vunita"]) * float(value["platos"]["canti"])

			menudeta = Menusdeta(**value["platos"])

			response["data"].append({
				"DT_RowId": "row_1",
				"ingredientes" : {
					"it" : str(menudeta.it),
					"cingre" : str(menudeta.cingre.cingre),
					"canti" : str(menudeta.canti),
					"vunita" : str(menudeta.vunita),
					"vtotal" : str(menudeta.vtotal),
				},
				"cingres" : {
					"name" : str(menudeta.cingre.ningre)
				}
			})

			menudeta.save(using=using)

			menu.vttotal += decimal.Decimal(menudeta.vtotal)
			menu.save(using=using)

	response["menu"] = json.loads(serializers.serialize("json", list([menu]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]
	return response

def MenuDetailUpdate(data,using):
	response = { "data" : []  }

	for key, value in data:
		ingrediente = Ingredientes.objects.using(using).get(pk=value["platos"]["cingre"])
		plato = Platos.objects.using(using).get(pk=value["platos"]["cplato"])

		value["platos"]["cingre"] = ingrediente
		value["platos"]["cplato"] = plato
		platodeta = Platosdeta.objects.using(using).get(cplato=plato.cplato,cingre=ingrediente.cingre)

		plato.vttotal -= decimal.Decimal(platodeta.vtotal)

		platodeta.canti = float(platodeta.canti)
		platodeta.vunita = float(platodeta.vunita)

		platodeta.vtotal = platodeta.canti * platodeta.vunita

		platodeta.canti = float(value["platos"]["canti"])
		platodeta.vunita = float(value["platos"]["vunita"])
		platodeta.vtotal = float(value["platos"]["canti"]) * float(value["platos"]["vunita"])

		response["data"].append({
			"DT_RowId": "row_1",
			"ingredientes" : {
				"it" : platodeta.it,
				"cingre" : platodeta.cingre.cingre,
				"canti" : platodeta.canti,
				"vunita" : platodeta.vunita,
				"vtotal" : platodeta.vtotal,
			},
			"cingres" : {
				"name" : str(platodeta.cingre.ningre)
			}
		})

		platodeta.save(using=using)

		plato.vttotal += decimal.Decimal(platodeta.vtotal)
		plato.save(using=using)

	response["plato"] = json.loads(serializers.serialize("json", list([plato]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]

	return response

def MenuDetailRemove(data,using):
	response = { "data" : []  }

	for key, value in data:
		ingrediente = Ingredientes.objects.using(using).get(pk=value["platos"]["cingre"])
		plato = Platos.objects.using(using).get(pk=value["platos"]["cplato"])
		platodeta = Platosdeta.objects.using(using).get(cplato=plato.cplato,cingre=ingrediente.cingre)

		response["data"].append({})

		platodeta.delete(using=using)

		plato.vttotal -= decimal.Decimal(platodeta.vtotal)
		plato.save(using=using)

	response["plato"] = json.loads(serializers.serialize("json", list([plato]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]

	return response

@csrf_exempt
def GetMenuDetail(request,pk):
	deta = Menusdeta.objects.using(request.db).filter(cmenu=pk)

	#ingredientes = Ingredientes.objects.using(request.db).all()
	#ingredientes_json = []

	#for ingrediente in ingredientes:
	#	ingredientes_json.append({"value":ingrediente.cingre,"label":ingrediente.ningre})

	data = {
		"data" :[] ,
		#"options": {"ingredientes.cingre": ingredientes_json}
	}
	for item in deta:
		data["data"].append({
				"DT_RowId": "row_1",
				"ingredientes" : {
					"cplato" : str(item.cplato.cplato),
					"it" : str(item.it),
					"canti" : str(item.canti),
					"vunita" : str(item.vunita),
					"vtotal" : str(item.vtotal),
				},
				#"cplatos" : {
				#	"name" : str(item.cplato.ningre)
				#}
			})
	return HttpResponse(json.dumps(data), content_type="application/json")
