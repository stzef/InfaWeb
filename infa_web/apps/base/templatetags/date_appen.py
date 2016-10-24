from infa_web.apps.base.constantes import CESDO_ACTIVO
from infa_web.apps.movimientos.models import *
from django.template import Context, Template
from infa_web.apps.facturacion.views import *
from infa_web.apps.base.models import *
from infa_web.apps.base.utils import *
from django.db.models import Sum
from django import template
import os

register = template.Library()

@register.simple_tag
#def date_appen(format_string):
def date_appen():
	return os.environ["date_appen"]
	#return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def boton_nuevo(btn_n=True,btn_s=True,btn_l=True):
	stringHTML = """<div class="text-center">
						<div class="btn-group">
							{{}}
						</div>
					</div>"""

	buttons = ""

	if btn_n:
		stringHTML_btn_n = """<button class="btn btn-app btn-info" type="reset">
								<i class="fa fa-plus-square-o"></i>Nuevo
							</button>"""
		t_stringHTML_btn_n = Template(stringHTML_btn_n)
		html_btn_n = t_stringHTML_btn_n.render(Context({}))

		buttons += str(html_btn_n)

	if btn_s:
		stringHTML_btn_s = """<button class="btn btn-app" type="submit">
								<i class="fa fa-plus-square-o"></i>Guardar
							</button>"""
		t_stringHTML_btn_s = Template(stringHTML_btn_s)
		html_btn_s = t_stringHTML_btn_s.render(Context({}))

		buttons += str(html_btn_s)

	if btn_l:
		stringHTML_btn_l = """<a data-new-window class="btn btn-app" href=""><i class="fa fa-list"></i>Listar</a>"""
		t_stringHTML_btn_l = Template(stringHTML_btn_l)
		html_btn_l = t_stringHTML_btn_l.render(Context({}))

		buttons += str(html_btn_l)

	print type(buttons)

	stringHTML = """<div class="text-center">
						<div class="btn-group">
							<button class="btn btn-app btn-info" type="reset">
								<i class="fa fa-plus-square-o"></i>Nuevo
							</button>
							<button class="btn btn-app" type="submit">
								<i class="fa fa-plus-square-o"></i>Guardar
							</button>
							<a data-new-window class="btn btn-app" href="{{href}}"><i class="fa fa-list"></i>Listar</a>
						</div>
					</div>"""

	t = Template(stringHTML)

	c = Context({'href': '#'})
	html = t.render(c)
	return html

@register.assignment_tag
def define(val = None):
	return val

@register.filter
def multiply(val_1, val_2):
	return "{:.2f}".format(val_1 * val_2)

@register.filter
def subtotal_group_invini(group):
	return "{:.2f}".format(sum((data.vunita * data.canti) for data in group))

@register.filter
def return_tot_movi(list_movi):
	return sum(movi.vttotal for movi in list_movi)

@register.filter
def saldo_cartera(citerce, request_db):
	ctimo_abono = ctimo_billing('ctimo_ab_billing', request_db)
	ctimo_cartera = ctimo_billing('ctimo_cxc_billing', request_db)
	cesdo = get_or_none(Esdo, request_db, cesdo = CESDO_ACTIVO)
	movi = Movi.objects.using(request_db).filter(citerce = citerce, cesdo = cesdo)
	movi_ab = movi.filter(ctimo = ctimo_abono).aggregate(val_tot = Sum('vttotal'))['val_tot']
	movi_cr = movi.filter(ctimo = ctimo_cartera).aggregate(val_tot = Sum('vttotal'))['val_tot']
	print cesdo
	return float(movi_cr) - float(movi_ab if movi_ab is not None else 0)

@register.filter
def get_saldo(cmovi, request_db):
	ctimo_cartera = ctimo_billing('ctimo_cxc_billing', request_db)
	cesdo = get_or_none(Esdo, request_db, cesdo = CESDO_ACTIVO)
	if cmovi.cmovi.ctimo == ctimo_cartera:
		value = cmovi.vmovi
	else:
		movi_original = Movi.objects.using(request_db).get(cesdo = cesdo, cmovi = cmovi.docrefe).vttotal
		movi_abono = Movideta.objects.using(request_db).filter(cmovi__cesdo = cesdo, docrefe = cmovi.docrefe, cmovi__fmovi__lte = cmovi.cmovi.fmovi).aggregate(val_tot = Sum('vmovi'))['val_tot']
		value = movi_original - movi_abono
	return value

@register.filter
def get_total_saldo(citerce, request_db):
	ctimo_cartera = ctimo_billing('ctimo_cxc_billing', request_db)
	ctimo_abono = ctimo_billing('ctimo_ab_billing', request_db)
	cesdo = get_or_none(Esdo, request_db, cesdo = CESDO_ACTIVO)
	movi_cartera = Movi.objects.using(request_db).filter(cesdo = cesdo, citerce = citerce.citerce, ctimo = ctimo_cartera).aggregate(val_tot = Sum('vttotal'))['val_tot']
	movi_abono = Movideta.objects.using(request_db).filter(cmovi__cesdo = cesdo, cmovi__citerce = citerce.citerce, cmovi__ctimo = ctimo_abono).aggregate(val_tot = Sum('vmovi'))['val_tot']
	value = movi_cartera - (movi_abono if movi_abono is not None else 0)
	return value

@register.filter
def total_abono(citerce, request_db):
	ctimo_abono = ctimo_billing('ctimo_ab_billing', request_db)
	cesdo = get_or_none(Esdo, request_db, cesdo = CESDO_ACTIVO)
	movi = Movi.objects.using(request_db).filter(cesdo = cesdo, citerce = citerce)
	movi_ab = movi.filter(ctimo = ctimo_abono).aggregate(val_tot = Sum('vttotal'))['val_tot']
	return (movi_ab if movi_ab is not None else 0)