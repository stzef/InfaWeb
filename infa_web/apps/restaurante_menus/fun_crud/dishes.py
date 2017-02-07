from infa_web.apps.restaurante_menus.models import *
from django.db.models import Max
from django.core import serializers
from django.http import HttpResponse


import decimal
import json
from django.views.decorators.csrf import csrf_exempt



def DishDetailCreate(data,using):
	response = { "data" : []  }

	for key, value in data:
		ingrediente = Ingredientes.objects.using(using).get(pk=value["ingredientes"]["cingre"])
		plato = Platos.objects.using(using).get(pk=value["ingredientes"]["cplato"])

		if not Platosdeta.objects.using(using).filter(cingre=ingrediente,cplato=plato).exists():
			it = Platosdeta.objects.using(using).filter(cplato=plato).aggregate(Max('it'))
			if it["it__max"]:
				it = int(it["it__max"]) + 1
			else:
				it = 1


			value["ingredientes"]["cingre"] = ingrediente
			value["ingredientes"]["cplato"] = plato

			value["ingredientes"]["it"] = it

			value["ingredientes"]["vunita"] = ingrediente.vcosto
			value["ingredientes"]["vtotal"] = float(value["ingredientes"]["vunita"]) * float(value["ingredientes"]["canti"])

			platodeta = Platosdeta(**value["ingredientes"])

			response["data"].append({
				"DT_RowId": "row_1",
				"ingredientes" : {
					"it" : str(platodeta.it),
					"cingre" : str(platodeta.cingre.cingre),
					"canti" : str(platodeta.canti),
					"vunita" : str(platodeta.vunita),
					"vtotal" : str(platodeta.vtotal),
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

def DishDetailUpdate(data,using):
	response = { "data" : []  }

	for key, value in data:
		ingrediente = Ingredientes.objects.using(using).get(pk=value["ingredientes"]["cingre"])
		plato = Platos.objects.using(using).get(pk=value["ingredientes"]["cplato"])

		value["ingredientes"]["cingre"] = ingrediente
		value["ingredientes"]["cplato"] = plato
		platodeta = Platosdeta.objects.using(using).get(cplato=plato.cplato,cingre=ingrediente.cingre)

		plato.vttotal -= decimal.Decimal(platodeta.vtotal)

		platodeta.canti = float(platodeta.canti)
		platodeta.vunita = float(platodeta.vunita)

		platodeta.vtotal = platodeta.canti * platodeta.vunita

		platodeta.canti = float(value["ingredientes"]["canti"])
		platodeta.vunita = float(value["ingredientes"]["vunita"])
		platodeta.vtotal = float(value["ingredientes"]["canti"]) * float(value["ingredientes"]["vunita"])

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

def DishDetailRemove(data,using):
	response = { "data" : []  }

	for key, value in data:
		ingrediente = Ingredientes.objects.using(using).get(pk=value["ingredientes"]["cingre"])
		plato = Platos.objects.using(using).get(pk=value["ingredientes"]["cplato"])
		platodeta = Platosdeta.objects.using(using).get(cplato=plato.cplato,cingre=ingrediente.cingre)

		response["data"].append({})

		platodeta.delete(using=using)

		plato.vttotal -= decimal.Decimal(platodeta.vtotal)
		plato.save(using=using)

	response["plato"] = json.loads(serializers.serialize("json", list([plato]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]

	return response

@csrf_exempt
def GetDishDetail(request,pk):
	deta = Platosdeta.objects.using(request.db).filter(cplato=pk)

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
					"cingre" : str(item.cingre.cingre),
					"it" : str(item.it),
					"canti" : str(item.canti),
					"vunita" : str(item.vunita),
					"vtotal" : str(item.vtotal),
				},
				#"cingres" : {
				#	"name" : str(item.cingre.ningre)
				#}
			})
	return HttpResponse(json.dumps(data), content_type="application/json")
