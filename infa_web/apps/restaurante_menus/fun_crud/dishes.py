from infa_web.apps.restaurante_menus.models import *
from django.db.models import Max
from django.core import serializers
from django.http import HttpResponse


import decimal
import json
from django.views.decorators.csrf import csrf_exempt

def DishDetailCreate(data,using):
	response = { "data" : [] , "message" : False }

	for key, value in data:
		del value["ningre"]
		ingrediente = Ingredientes.objects.using(using).get(pk=value["cingre"])
		plato = Platos.objects.using(using).get(pk=value["cplato"])

		if not Platosdeta.objects.using(using).filter(cingre=ingrediente,cplato=plato).exists():
			it = Platosdeta.objects.using(using).filter(cplato=plato).aggregate(Max('it'))
			if it["it__max"]:
				it = int(it["it__max"]) + 1
			else:
				it = 1


			value["cingre"] = ingrediente
			value["cplato"] = plato

			value["it"] = it

			value["vunita"] = ingrediente.vcosto
			value["vtotal"] = float(value["vunita"]) * float(value["canti"])

			value["cunidad"] = ingrediente.cunidad


			platodeta = Platosdeta(**value)

			response["data"].append({
				"DT_RowId": "row_1",
				"ingredientes" : {
					"it" : str(platodeta.it),
					"cingre" : str(platodeta.cingre.cingre),
					"ningre" : str(platodeta.cingre.ningre),
					"canti" : str(platodeta.canti),
					"vunita" : str(platodeta.vunita),
					"vtotal" : str(platodeta.vtotal),
					"cunidad" : str(platodeta.cingre.cunidad.nunidad),
				},
				"cingres" : {
					"name" : str(platodeta.cingre.ningre)
				}
			})

			platodeta.save(using=using)

			plato.vttotal += decimal.Decimal(platodeta.vtotal)
			plato.save(using=using)
		else:
			response["message"] = {"text":"El ingrediente ya se encuentra registrado en el plato","type":"info"}

	response["plato"] = json.loads(serializers.serialize("json", list([plato]),use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]
	return response

def DishDetailUpdate(data,using):
	response = { "data" : []  }

	for key, value in data:
		ingrediente = Ingredientes.objects.using(using).get(pk=value["cingre"])
		plato = Platos.objects.using(using).get(pk=value["cplato"])

		value["cingre"] = ingrediente
		value["cplato"] = plato
		platodeta = Platosdeta.objects.using(using).get(cplato=plato.cplato,cingre=ingrediente.cingre)

		plato.vttotal -= decimal.Decimal(platodeta.vtotal)

		platodeta.canti = float(platodeta.canti)
		platodeta.vunita = float(platodeta.vunita)

		platodeta.vtotal = platodeta.canti * platodeta.vunita

		platodeta.canti = float(value["canti"])
		platodeta.vunita = float(value["vunita"])
		platodeta.vtotal = float(value["canti"]) * float(value["vunita"])

		value["cunidad"] = ingrediente.cunidad

		response["data"].append({
			"DT_RowId": "row_1",
			"ingredientes" : {
				"it" : platodeta.it,
				"cingre" : platodeta.cingre.cingre,
				"ningre" : platodeta.cingre.ningre,
				"canti" : platodeta.canti,
				"vunita" : platodeta.vunita,
				"vtotal" : platodeta.vtotal,
				"cunidad" : platodeta.cingre.cunidad.nunidad,
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
		#del value["cunidad"]
		ingrediente = Ingredientes.objects.using(using).get(pk=value["cingre"])
		plato = Platos.objects.using(using).get(pk=value["cplato"])
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
					"ningre" : str(item.cingre.ningre),
					"it" : str(item.it),
					"canti" : str(item.canti),
					"vunita" : str(item.vunita),
					"vtotal" : str(item.vtotal),
					"cunidad" : str(item.cingre.cunidad.nunidad),
				},
				#"cingres" : {
				#	"name" : str(item.cingre.ningre)
				#}
			})
	return HttpResponse(json.dumps(data), content_type="application/json")
