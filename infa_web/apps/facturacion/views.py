from django.shortcuts import render,render_to_response 
from django.views.generic import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy 
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import json

from infa_web.apps.facturacion.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.articulos.models import *
from infa_web.apps.facturacion.forms import *
from infa_web.apps.base.forms import *

def sum_fac(value):
	value_sum = str(int(value[2:])+1)
	cant_space = 8-int(len(value_sum))
	return '--'+(cant_space*'0')+value_sum

@csrf_exempt
def BillSave(request):
	data = json.loads(request.body)
	response = {}
	fac_pk = ""
	response["error"] = False
	response["message"] = "Factura Guardada con Exito"

	print (json.dumps(data,indent=4))
	#print json.dumps(data, indent=4)

	try:
		value = Fac.objects.all().latest('pk')
		fac_pk = sum_fac(value.pk)
	except Fac.DoesNotExist:
		fac_pk = '--00001000'

	citerce = Tercero.objects.get(pk = data['citerce'])
	cesdo = Esdo.objects.get(pk = data['cesdo'])
	ctifopa = Tifopa.objects.get(pk = data['ctifopa'])
	bancotar = Banfopa.objects.get(pk = data['bancotar'])
	bancochq = Banfopa.objects.get(pk = data['bancochq'])
	ccaja = Caja.objects.get(pk = data['ccaja'])
	cvende = Vende.objects.get(pk = data['cvende'])
	cdomici = Domici.objects.get(pk = data['cdomici'])
	cemdor = Emdor.objects.get(pk = data['cemdor'])
	fac = Fac(
			cfac = fac_pk, 
			femi = data['femi'], 
			citerce = citerce, 
			cesdo = cesdo, 
			fpago = fpago, 
			ctifopa = ctifopa,
			descri = '-',
			vtbase = data['vtbase'],
			vtiva = data['vtiva'],
			vflete = data['vflete'],
			vdescu = data['vdescu'],
			vttotal = data['vttotal'],
			vefe = data['vefe'],
			vtar = data['vtar'],
			doctar = data['doctar'],
			bancotar = bancotar,
			vchq = data['vchq'],
			docchq = data['docchq'],
			bancochq = bancochq,
			ventre = data['ventre'],
			vcambio = data['vcambio'],
			ccaja = ccaja,
			cvende = cvende,
			cdomici = cdomici,
			tpordes = 0,
			cemdor = cemdor,
			vncre = 0,
			doccre = '-',
			brtefte = data['brtefte'],
			prtefte = data['prtefte'],
			vrtefte = data['vrtefte']
		)
	fac.save()

	mvsa = Mvsa(
			fmvsa = data['femi'],
			docrefe = fac.pk,
			citerce = citerce,
			ctimo = ccaja.ctimocj,
			cesdo = cesdo,
			vttotal = data['vttotal'],
			descri = '-'
		)
	mvsa.save()

	for data_deta in data["facdeta"]:
		carlos = Arlo.objects.get(pk = data_deta['carlos'])
		civa = Iva.objects.get(pk = data_deta['civa'])
		vt = data_deta['vunita'] * data_deta['canti']
		viva = vt * civa.poriva

		fac_deta = Facdeta(
				cfac = fac,
				itfac = data_deta['itfac'],
				carlos = carlos,
				nlargo = carlos.nlargo,
				ncorto = carlos.ncorto,
				canti = data_deta['canti'],
				civa = civa,
				niva = civa.niva,
				poriva = civa.poriva,
				pordes = data_deta['pordes'],
				vunita = data_deta['vunita'],
				viva = viva,
				vbase = vt,
				vtotal = (vt + viva),
				pvtafull = carlos.pvta1, 
				vcosto = carlos.vcosto1
			)

		mvsa_deta = Mvsadeta(
				cmvsa = mvsa,
				it = data_deta['itfac'],
				carlos = carlos,
				nlargo = carlos.nlargo,
				canti = data_deta['canti'],
				vunita = data_deta['vunita'],
				vtotal = (vt + viva)
			)

		mvsa_deta.save()
		fac_deta.save()

	#Crear Movi
	#Crear Movideta

	return HttpResponse(json.dumps(response), "application/json")

class BillCreate(CreateView):
	model = Fac
	template_name = "facturacion/billing.html"
	form_class = FacForm

	def get_context_data(self,**kwargs):
		context = super(BillCreate, self).get_context_data(**kwargs)

		context['title'] = "Facturar"
		form_movement_detail = FacdetaForm()
		context['form_movement_detail'] = form_movement_detail

		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('save-bill')

		return context

def bill_proccess_view_annulment(request):
	form = CommonForm()
	return render(request,"facturacion/procesos/annulment.html",{"form":form})

def bill_proccess_fn_annulment(request):
	data = json.loads(request.body)

	return HttpResponse(json.dumps({"message":"Se realizo exitosamente el cambio"}), content_type="application/json",status=200)
