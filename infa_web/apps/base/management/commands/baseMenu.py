# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
from datetime import datetime

from infa_web.apps.base.constantes import *
from infa_web.apps.base.models import NavMenus, Modules

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			'--database',
			action='store',
			dest='database',
			default="default",
			help='DB for connection',
		)
	def handle(self, *args, **options):

		name_db =  options["database"]
		print "DB Actual '%s'" % name_db

		prosiga_bajo_su_responsabilidad = False

		confirmation = raw_input("Seguro? (Si/No) ")
		if(confirmation == "Si"):
			prosiga_bajo_su_responsabilidad = True

		if(prosiga_bajo_su_responsabilidad):
			NavMenus.objects.using(name_db).all().delete()

			facturacion = Modules.objects.using(name_db).get(smodule="F")
			inventario = Modules.objects.using(name_db).get(smodule="I")
			mod_pos = Modules.objects.using(name_db).get(smodule="P")
			mod_general = Modules.objects.using(name_db).get(smodule="G")
			mod_adm = Modules.objects.using(name_db).get(smodule="A")
			mod_cartera = Modules.objects.using(name_db).get(smodule="CAR")
			mod_restaurante = Modules.objects.using(name_db).get(smodule="R")

			m_facturacion = NavMenus.objects.using(name_db).create(
				name="Facturacion",
				main=True,
				enabled=True,
				anchor=True,
				url=None,
				permission=None,
				module=facturacion,
				general=False,
				father=None,
				icon='fa-dollar',
			)
			m_facturacion_facturar = NavMenus.objects.using(name_db).create(
				name="Facturar",
				main=False,
				enabled=True,
				anchor=False,
				url='create-bill',
				permission='facturacion.add_fac',
				module=facturacion,
				general=False,
				father=m_facturacion,
				icon='fa-dollar',
			)
			m_facturacion_reportes = NavMenus.objects.using(name_db).create(
				name="Reportes",
				main=False,
				enabled=True,
				anchor=True,
				url=None,
				permission=None,
				module=facturacion,
				general=False,
				father=m_facturacion,
				icon='fa-sticky-note-o',
			)
			m_facturacion_reportes_1 = NavMenus.objects.using(name_db).create(
				name="Ventas",
				main=False,
				enabled=True,
				anchor=False,
				url='report_view_bill',
				permission='facturacion.report_fac_bill',
				module=facturacion,
				general=False,
				father=m_facturacion_reportes,
				icon='fa-sticky-note-o',
			)
			m_facturacion_reportes_2 = NavMenus.objects.using(name_db).create(
				name="Ventas por Formas de Pago",
				main=False,
				enabled=True,
				anchor=False,
				url='report_view_bill_payment_methods',
				permission='facturacion.report_fac_bill_payment',
				module=facturacion,
				general=False,
				father=m_facturacion_reportes,
				icon='fa-sticky-note-o',
			)

			m_inventario = NavMenus.objects.using(name_db).create(
				name = 'Inventario',
				main = True,
				enabled=True,
				anchor=True,
				url = None,
				permission = None,
				module = inventario,
				general=False,
				father = None,
				icon = 'fa-list-alt',
			)
			m_inventario_articulos = NavMenus.objects.using(name_db).create(
				name = 'Articulos',
				main = False,
				enabled=True,
				anchor=False,
				url = 'add-article',
				permission = 'articulos.add_arlo',
				module = inventario,
				general=False,
				father = m_inventario,
				icon = 'fa-archive',
				quick_access = True,
			)
			m_inventario_inv_inicial = NavMenus.objects.using(name_db).create(
				name = 'Inventario Inicial',
				main = False,
				enabled=True,
				anchor=False,
				url = 'inventory_list',
				permission = 'inventarios.add_invinicab',
				module = inventario,
				general=False,
				father = m_inventario,
				icon = 'fa-list-alt',
			)
			m_inventario_entradas = NavMenus.objects.using(name_db).create(
				name = 'Entrada',
				main = False,
				enabled=True,
				anchor=False,
				url = 'add-input-movement',
				permission = 'movimientos.add_mven',
				module = inventario,
				general=False,
				father = m_inventario,
				icon = 'fa-arrow-right',
			)
			m_inventario_salidas = NavMenus.objects.using(name_db).create(
				name = 'Salida',
				main = False,
				enabled=True,
				anchor=False,
				url = 'add-output-movement',
				permission = 'movimientos.add_mvsa',
				module = inventario,
				general=False,
				father = m_inventario,
				icon = 'fa-arrow-left',
			)

			m_pos = NavMenus.objects.using(name_db).create(
				name = 'POS',
				main = True,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = None,
				icon = 'fa-money',
				module = mod_pos,
			)
			m_pos_facturar = NavMenus.objects.using(name_db).create(
				permission = 'facturacion.add_fac_pos',
				url = 'create-pos',
				icon = 'fa-dollar',
				name = 'Facturar',
				module = mod_pos,
				main = False,
				enabled = True,
				anchor = False,
				general=False,
				father = m_pos,
				quick_access = True,
			)

			m_basicos = NavMenus.objects.using(name_db).create(
				name = 'Basicos',
				main = True,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = None,
				icon = 'fa-circle-o',
				module = mod_general,
			)
			m_basicos_Caja = NavMenus.objects.using(name_db).create(
				permission = 'base.add_caja',
				url = 'add-caja',
				icon = 'fa-square',
				name = 'Caja',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)
			m_basicos_Talonarios = NavMenus.objects.using(name_db).create(
				permission = 'base.add_talo',
				url = 'add-cheque-book',
				icon = 'fa-list',
				name = 'Talonarios',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)
			m_basicos_Sucursales = NavMenus.objects.using(name_db).create(
				permission = 'base.add_sucursales',
				url = 'add-branch',
				icon = 'fa-code-fork',
				name = 'Sucursales',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)
			m_basicos_Terceros = NavMenus.objects.using(name_db).create(
				permission = 'terceros.add_tercero',
				url = 'add-third-party',
				icon = 'fa-users',
				name = 'Terceros',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)
			m_basicos_Marcas = NavMenus.objects.using(name_db).create(
				permission = 'articulos.add_marca',
				url = 'add-brand',
				icon = 'fa-circle-o',
				name = 'Marcas',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)
			m_basicos_Grupos = NavMenus.objects.using(name_db).create(
				permission = 'articulos.add_gpo',
				url = 'add-group',
				icon = 'fa-circle-o',
				name = 'Grupos',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)
			m_basicos_Unidades = NavMenus.objects.using(name_db).create(
				permission = 'articulos.add_unidades',
				url = 'add-unit',
				icon = 'fa-circle-o',
				name = 'Unidades',
				father = m_basicos,
				general = False,
				enabled = True,
				main = False,
				anchor = False,
				module = mod_general,
			)

			m_conf = NavMenus.objects.using(name_db).create(
				name = 'Configuracion',
				main = True,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = None,
				icon = 'fa-cog',
				module = mod_adm,
			)
			m_conf_parametros = NavMenus.objects.using(name_db).create(
				name = 'Parametros',
				main = False,
				enabled = True,
				anchor = False,
				url = 'list-parameter',
				permission = 'base.save_parameters',
				general=False,
				father = m_conf,
				icon = 'fa-cogs',
				module = mod_adm,
			)
			m_conf_anulaciones = NavMenus.objects.using(name_db).create(
				name = 'Anulaciones',
				main = False,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = m_conf,
				icon = 'fa-wrench',
				module = mod_adm,
			)
			m_conf_anulaciones_mov_inv = NavMenus.objects.using(name_db).create(
				name = 'Movimientos de Inventario',
				main = False,
				enabled = True,
				anchor = False,
				url = 'proccess_view_annulment',
				permission = 'movimientos.change_mven',
				general=False,
				father = m_conf_anulaciones,
				icon = 'fa-arrows-h',
				module = mod_adm,
			)
			m_conf_anulaciones_factura = NavMenus.objects.using(name_db).create(
				name = 'Facturas',
				main = False,
				enabled = True,
				anchor = False,
				url = 'bill_proccess_view_annulment',
				permission = 'facturacion.change_fac',
				general=False,
				father = m_conf_anulaciones,
				icon = 'fa-money',
				module = mod_adm,
			)
			m_conf_anulaciones_comandas = NavMenus.objects.using(name_db).create(
				name = 'Comandas',
				main = False,
				enabled = True,
				anchor = False,
				url = 'order-command-proccess-view-annulment',
				permission = 'restaurante_comandas.change_coda',
				general=False,
				father = m_conf_anulaciones,
				icon = 'fa-money',
				module = mod_adm,
			)
			m_conf_usuarios = NavMenus.objects.using(name_db).create(
				name = 'Usuarios',
				main = False,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = m_conf,
				icon = 'fa-users',
				module = mod_adm,
			)
			m_conf_usuarios_nuevo = NavMenus.objects.using(name_db).create(
				name = 'Nuevo',
				main = False,
				enabled = True,
				anchor = False,
				url = 'registrar-usuario',
				permission = 'auth.add_user',
				general=False,
				father = m_conf_usuarios,
				icon = 'fa-arrows-h',
				module = mod_adm,
			)
			m_conf_usuarios_administrar = NavMenus.objects.using(name_db).create(
				name = 'Administrar',
				main = False,
				enabled = True,
				anchor = False,
				url = 'administrar-usuarios',
				permission = 'auth.add_user',
				general=False,
				father = m_conf_usuarios,
				icon = 'fa-money',
				module = mod_adm,
			)

			m_cartera = NavMenus.objects.using(name_db).create(
				name = 'Cartera por Cobrar',
				main = True,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = None,
				icon = 'fa-usd',
				module = mod_cartera,
			)
			m_cartera_lista = NavMenus.objects.using(name_db).create(
				name = 'Lista de cartera',
				main = False,
				enabled = True,
				anchor = False,
				url = 'list-cartera',
				permission = None,
				general=False,
				father = m_cartera,
				icon = 'fa-list',
				module = mod_cartera,
			)

			m_restaurante = NavMenus.objects.using(name_db).create(
				name = 'Restaurante',
				main = True,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = None,
				icon = 'fa-list-alt',
				module = mod_restaurante,
			)
			m_restaurante_basicos = NavMenus.objects.using(name_db).create(
				name = 'Basicos',
				main = False,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = m_restaurante,
				icon = 'fa-list-alt',
				module = mod_restaurante,
			)
			m_restaurante_basicos_Ingredientes = NavMenus.objects.using(name_db).create(
				name = 'Ingredientes',
				main = False,
				enabled = True,
				anchor = False,
				url = 'add-ingredient',
				permission = 'restaurante_menus.add_ingredientes',
				general=False,
				father = m_restaurante_basicos,
				icon = 'fa-archive',
				module = mod_restaurante,
			)
			m_restaurante_basicos_Platos = NavMenus.objects.using(name_db).create(
				name = 'Platos',
				main = False,
				enabled = True,
				anchor = False,
				url = 'add-dish',
				permission = 'restaurante_menus.add_platos',
				general=False,
				father = m_restaurante_basicos,
				icon = 'fa-cutlery',
				module = mod_restaurante,
			)
			m_restaurante_basicos_Menu = NavMenus.objects.using(name_db).create(
				name = 'Menu',
				main = False,
				enabled = True,
				anchor = False,
				url = 'add-menu',
				permission = 'articulos.add_arlo',
				general=False,
				father = m_restaurante_basicos,
				icon = 'fa-list-alt',
				module = mod_restaurante,
			)
			m_restaurante_comandas = NavMenus.objects.using(name_db).create(
				name = 'Comandas',
				main = False,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = m_restaurante,
				icon = 'fa-list-alt',
				module = mod_restaurante,
			)
			m_restaurante_comandas_Tomar = NavMenus.objects.using(name_db).create(
				name = 'Tomar',
				main = False,
				enabled = True,
				anchor = False,
				url = 'take-order',
				permission = 'restaurante_comandas.add_coda',
				general=False,
				father = m_restaurante_comandas,
				icon = 'fa-archive',
				module = mod_restaurante,
				quick_access = True,
			)
			m_restaurante_comandas_Rack = NavMenus.objects.using(name_db).create(
				name = 'Rack',
				main = False,
				enabled = True,
				anchor = False,
				url = 'order-summary',
				permission = 'restaurante_comandas.add_coda',
				general=False,
				father = m_restaurante_comandas,
				icon = 'fa-cutlery',
				module = mod_restaurante,
				quick_access = True,
			)
			m_restaurante_reportes = NavMenus.objects.using(name_db).create(
				name = 'Reportes',
				main = False,
				enabled = True,
				anchor = True,
				url = None,
				permission = None,
				general=False,
				father = m_restaurante,
				icon = 'fa-list-alt',
				module = mod_restaurante,
			)
			m_restaurante_reportes_cuentas1 = NavMenus.objects.using(name_db).create(
				name = 'Reporte de Cuentas',
				main = False,
				enabled = True,
				anchor = False,
				url = 'report_view_accounts',
				permission = 'restaurante_comandas.report_resupedi',
				general=False,
				father = m_restaurante_reportes,
				icon = 'fa-archive',
				module = mod_restaurante,
			)

		else:
			print "Operación Cancelada."

