var selector_element_focus_on_totalizar = "[name=ventre]"

var mode_view = $("#mode_view").val()
var current_arlo = null //Articulo(Objeto DB) que se selecciona en el #form_deta_movement
var current_tercero = null //Tercero(Objeto DB) que se selecciona en el #id_citerce
var pvta_menor = null
var it = 1
var containerMessages = $("#messages-container")
$('#id_itfac').val(it)
calcular_total()

var text_message_ingrese_medios_pago = "No ha ingresado ningún Medio de Pago."
var text_message_ingrese_articulos = "No ha ingresado ningún Artículo."
var text_message_ventre_menor_total = "El Valor Entrado es menor al Valor Total."
var text_message_descuento_mayor_vttotal = "No puede realizar un Descuento Mayor al Valor Total."
var text_message_error_request = "Ha ocurrido un error en el proceso."
var text_message_vttotal_mayor_cero = "El Valor Total debe ser mayor a cero."
var text_message_seleccione_articulo = "Seleccione un artículo."
var text_message_seleccione_tercero = "Seleccione un Tercero."
var text_message_menor_igual_cero = "El Valor a Pagar no puede ser menor o igual a cero."
var text_message_tope_descuento = "El tope de descuento es " + data_validation.top_discount_bills
var text_message_vpago_mayor_vttotal = "El Valor a Pagar no puede ser mayor al Valor Total."
var text_message_numero_maximo_items_por_factura = "El número máximo de ítems por factura para este usuario segun el talonario ya se ha superado."
text_message_vpago_menor_vttotal = "El Valor de Pago no puede ser menor al Valor Total."

Number.prototype.format = function(n, x) {
	var re = '\\d(?=(\\d{' + (x || 3) + '})+' + (n > 0 ? '\\.' : '$') + ')';
	return this.toFixed(Math.max(0, ~~n)).replace(new RegExp(re, 'g'), '$&,');
};

$(document).on("keyup", "#id_canti", function(e){
	var this_value = isNaN(parseFloat($(this).val())) ? 0: parseFloat($(this).val());
	var value_tot = this_value * $('#id_vunita').custom_format_val();
	$('#id_vtotal').val(value_tot).trigger("change")
});

$(document).on("keyup", "#id_vunita", function(e){
	var this_value = isNaN(parseFloat($(this).custom_format_val())) ? 0: parseFloat($(this).custom_format_val());
	var value_tot = this_value * $('#id_canti').val()
	$('#id_vtotal').val(value_tot).trigger("change")
});

function print_bill(cfac){
	/*
		@param cfac String : codigo de factura a imprimir
		Abre una nueva ventana con la factura en pdf
	*/
	window.open("/bill/print?cfac=" + cfac)
}

function setValueFieldTerce(){
	/*

		#id_citerce : Identificacion del tercero
		[name=name__citerce] : Nombre del tercero

		En base a 'current_tercero' envia valores a los campos '#id_citerce','[name=name__citerce]'
		si current_arlo es null envia "","" Respectivamente
		por el contrario si no es null envia los valores del objeto del tercero.
	*/
	if(current_tercero){
		id_citerce = current_tercero.idterce
		name__citerce = current_tercero.rasocial
	}else{
		id_citerce = ""
		name__citerce = ""
	}
	$('#id_citerce').val(id_citerce)
	$("[name=name__citerce]").val(name__citerce)
}

function setValueFieldArlo(){
	/*
		[name=vunita] : Valor unitario del Articulo.
		[name=carlos] : Codigo del Articulo.
		[name=name__carlos] : Noombre del Articulo.
		[name=civa] : Codigo de Iva relacionado al Articulo.

		En base a 'current_arlo' envia valores a los campos '[name=vunita]','[name=carlos]','[name=name__carlos]','[name=civa]'
		si current_arlo es null envia "","","","" Respectivamente
		por el contrario si no es null envia los valores del objeto del articulo.
	*/
	$("[name=pordes]").val(0)

	$("[name=name__carlos]").prop("readonly",true)

	$("[name=vunita]").prop("readonly",false)
	$("[name=pordes]").prop("readonly",false)

	if(current_arlo){
		var name__carlos = current_arlo.nlargo
		var ivas_civa = current_arlo.ivas_civa
		if(current_arlo.ifedinom) $("[name=name__carlos]").prop("readonly",false)
		if(current_arlo.ifpvfijo) {
			$("[name=vunita]").prop("readonly",true)
			$("[name=pordes]").prop("readonly",true)
		}
	}else{
		var name__carlos = ""
		var ivas_civa = ""
		$("[name=vunita]").val("0").trigger("change")
		$("[name=carlos]").val("").focus()
	}
	$("[name=name__carlos]").val(name__carlos)
	$("[name=civa]").val(ivas_civa)
	calcular_valor_unitario()
	$('#id_canti').trigger('keyup');
}

function mostrar_modal_lista_precios(if_return_mpvta){
	/*
		Retorna el precio de venta menor (pvta_menor) del articulo actual (current_arlo)
		ó
		Muestra una ventana Modal con la lista de precios del articulo actual (current_arlo)
	*/
	$("#lista_precios .modal-body").empty()
	if(!current_arlo) return alert(text_message_seleccione_articulo)
	var table = $("<table class='table table table-striped'>")
		for (field in current_arlo){
			regexp = /pvta[0-9]/
			pvta_menor = current_arlo.pvta1
			if(regexp.test(field)){
				if(current_arlo[field] < pvta_menor){
					pvta_menor = current_arlo[field]
				}
				table.append(
					$("<tr>").append(
						$("<td>",{html:field.replace("pvta", 'Precio Venta ')}),
						$("<td>",{html:currencyFormat.format(current_arlo[field])})
					)
				)
			}
		}
		if(if_return_mpvta) return pvta_menor
		$("#lista_precios .modal-body").append("<p>Cantidad Actual: " + current_arlo.canti + "</p>")
		$("#lista_precios .modal-body").append(table)
		$("#lista_precios").modal("show")
}

function borrar_medios_pago_registrados(){
	$("#list_medios_pago").find("tbody").children().remove()
}
function borrar_articulos_registrados(){
	$("#list_items_mdeta").find("tbody").children().remove()
}

function show_modal_totalizar(){
	/*
		[name=ctifopa] : Forma de Pago
		[name=cmpago] : Medio de Pago
		[name=vmpago] : Valor Total del Medio e Pago
		[name=vttotal] : Valor Total de la Factura

		Abre la ventana Modal de Medios de Pago

		Validaciones
		Si [name=ctifopa] es igual a la forma de pago Contado
		Crea por defecto un registro(HTML <tr>) de la tabla(HTML <table>) COn la forma de pago Contada
			[name=cmpago] = Medio de pago Efectivo
			[name=vmpago] = [name=vttotal]
		Si no lo es simplemente abre la ventana modal en blanco
	*/
	var array_mvdeta = get_data_list("#list_items_mdeta")
	if(!array_mvdeta.length) return containerMessages.prepend(alertBootstrap(text_message_ingrese_articulos,"warning"))
	//$("#list_medios_pago table tbody tr").remove()

	if(mode_view != "edit") set_pago_completo_efectivo()

	$("#medios_pago").modal("show")
	//$("#medios_pago [name=cmpago]").focus()
	
}

function set_pago_completo_efectivo(){
	if($("[name=ctifopa]").val() == data_validation.formas_pago.FORMA_PAGO_CONTADO){
		borrar_medios_pago_registrados()
		$("#item_medio_pago [name=cmpago]").val(data_validation.medios_pago.MEDIO_PAGO_EFECTIVO).change()
		$("#item_medio_pago [name=vmpago]").val($("[name=vttotal]").custom_format_val()).trigger("change")
		$("#form_medios_pago").submit()
	}
}

function get_data_list(selector_list){/*Revisar*/
	/*
		Retorna un objeto con los valores de los atributos [data-name] y [data-value] de los tr de una tabla
		{
			tr1[data-name]: tr1[data-value],
			trn[data-name]: trn[data-value],
			...
			...
			...
		}
	*/
	return $(selector_list).find("tbody").find("tr").toArray().map(
		function(e){
			var data = {}
			$(e).children("[data-name]").toArray().forEach(
				function(e2){
					if($(e2).hasClass("value-currency")){
						data[$(e2).data("name")] = currencyFormat.sToN($(e2).data("value"))
					}else{
						data[$(e2).data("name")] = $(e2).data("value")
					}
				}
			)
			return data
		}
	)
}

function calcular_valor_cambio(){
	/*
		ventre: Valor entregado
		vttotal: Valor Total de la factura

		Validaciones
		Verifica que el ventre tenga valor
		Verifica que el vttotal tenga valor

		Calcula el valor de cambio de la factura
		Operacion = ventre - vttotal
	*/
	if(parseFloat($("[name=ventre]").custom_format_val()) && parseFloat($("[name=vttotal]").custom_format_val())){
		if(parseFloat($("[name=ventre]").custom_format_val()) >= parseFloat($("[name=vttotal]").custom_format_val())){
			var v_cambio = parseFloat($("[name=ventre]").custom_format_val()) - parseFloat($("[name=vttotal]").custom_format_val())
		}else{
			var v_cambio = ""
			$("#form_totales").prepend(alertBootstrap(text_message_ventre_menor_total,"info"))
		}
		$("[name=vcambio]").val(v_cambio).trigger("change")
	}
}

function calcular_valor_unitario(){
	/*
		pordes: Porcentaje de descuento del articulo
		vunita: Valor Unitario del articulo
		precio_venta: precio de venta que aplica para el tercero seleccionado(clipre: lista de precios)

		Validaciones
		Valida que se haya seleccionado un articulo en #form_deta_movement

		Calcula el valor unitario de un articulo
		Operacion = precio_venta - ( precio_venta * ( pordes / 100 ) )
	*/
	if(current_tercero && current_arlo){
		name_list_price = "pvta" + current_tercero.clipre
		var price_venta = parseFloat(current_arlo[name_list_price])
		var descuento = parseFloat($("#form_deta_movement [name=pordes]").val())

		var vunita = price_venta - (price_venta*(descuento/100))
		$("#form_deta_movement [name=vunita]").val(vunita).trigger("change")
	}
}

function calcular_total_flete(){
	/*
		brtefte: Valor base del flete
		prtefte: Porcentaje de descuento del flete
		vrtefte: valor total del flete

		Recalcula el valor total del flete de la factura
		Operacion = brtefte - ( brtefte * ( prtefte / 100 ) )
	*/
	var brtefte = parseFloat($("[name=brtefte]").custom_format_val())
	var prtefte = parseFloat($("[name=prtefte]").custom_format_val())

	var vrtefte = brtefte - (brtefte*(prtefte/100))
	$("[name=vrtefte]").val(vrtefte).trigger("change")
}

function calcular_vtbase_vtiva(){/*Revisar*/
	/*
		canti: cantidad a vender del articulo
		vunita: Valor unitario del articulo
		pordes: Porcentaje de descuento del articulo
		civa: IVA para el articulo

		vtbase: valor total de la base
		vtiva: valor total del iva

		Calcula el valor total de la base y el valor total del iva
		Operaciones
			vbase = precio_total / ( 1 + ( porcentaje_iva / 100 ) )
			viva = vbase * ( porcentaje_iva / 100 )

			vtbase += vbase
			vtiva += viva
	*/

	var vtbase = 0
	var vtiva = 0
	$("#list_items_mdeta tbody tr").toArray().forEach(function (e,i,a){
		var cantidad = parseFloat($(e).find("[data-name=canti]").data("value"))
		var precio = parseFloat(currencyFormat.sToN($(e).find("[data-name=vunita]").data("value")))
		//var porcentaje_descuento = parseFloat($(e).find("[data-name=pordes]").data("value"))

		var codigo_iva = parseFloat($(e).find("[data-name=civa]").data("value"))
		var porcentaje_iva = valores_iva[codigo_iva]

			/*
				Anotacion: El descuento no se aplica aqui oues el valor unitario ya lo tiene aplicado
			*/

		//var precio_total_sin_descuento = cantidad * precio
		//var precio_total = precio_total_sin_descuento - ( precio_total_sin_descuento * ( porcentaje_descuento / 100 ) )
		var precio_total = cantidad * precio

		var vbase = precio_total / ( 1 + ( porcentaje_iva / 100 ) )
		var viva = vbase * ( porcentaje_iva / 100 )

		vtbase += vbase
		vtiva += viva
	})
	return {vtbase: vtbase,vtiva: vtiva}
}

function calcular_total(){/*Revisar*/
	/*
		Calcula el valor Total de la Factura

		Recorre todos los times de la factura calculando el valor individual y sumandolos para luego operarlos con el descuento y los valores del flete
	*/
	var vttotal_items = 0
	var vttotal_local = 0
	$("#list_items_mdeta tbody tr")
		.toArray()
		.forEach(function(e){

			var temp_vunita = parseFloat(currencyFormat.sToN($(e).find("[data-name=vunita]").data("value")))
			var temp_canti = parseFloat($(e).find("[data-name=canti]").data("value"))

			/*
				Anotacion: El descuento no se aplica aqui oues el valor unitario ya lo tiene aplicado
			*/

			var vtotal_temp = temp_vunita * temp_canti
			vttotal_items += vtotal_temp
		}
	)
	var vflete = parseFloat($("[name=vflete]").custom_format_val())
	var porcentaje_descuento = parseFloat($("[name=vdescu]").val())
	var valor_descuento = parseFloat(currencyFormat.sToN($("[name=vdescu]").val()))


	vttotal_local_sin_descuento = vflete + vttotal_items
	vttotal_local = vttotal_local_sin_descuento - valor_descuento

	$("[name=vttotal]").val(vttotal_local).trigger("change")
	$("[data-mask=id_vttotal__mask]").val(vttotal_local).trigger("change")
	
	$("[name=ventre]").val(vttotal_local).trigger("change")
	if(valor_descuento > vttotal_local_sin_descuento){
		$("[name=vdescu]").val("0")
		return alert(text_message_descuento_mayor_vttotal)
	}

}

/* Operaciones */
$("[name=ventre]").change(function(){
	/*
		ventre: Valor entregado por el tercero apra pagar la factura

		Operacion
		Recalcula el valor del cambio.
	*/
	calcular_valor_cambio()
})

$("[name=vflete], [name=vdescu]").change(function(){
	/*
		vflete: Valor del flete
		vdescu: Valor del descuento general para la factura

		Operacion
		Recalcula el valor total de la factura.
	*/
	calcular_total()
})

$("[name=brtefte], [name=prtefte]").change(function(event){
	/*
		Operacion
		Recalcula el valor total del flete de la factura
	*/
	calcular_total_flete()
})
/* Operaciones */

/* Validaciones */
$("[name=canti]").change(function(){
	/*
		Validacion
		Valida si la cantidad ha vender dedterminado articulo es mayor a la cantidad maxima parametrizada, pregunta si se desa continuar o no
	*/	
	if(!current_arlo) {
		$(this).val("1")
		return alert(text_message_seleccione_articulo)
	}

	if(!data_validation.invoice_without_stock){
		if(parseFloat($(this).val()) > parseFloat(current_arlo.canti)){
			if(!confirm("La Cantidad " + current_arlo.canti + " no existe en el inventario actual, ¿Desea Continuar?")){
				$(this).val("").focus()
			}
		}
	}
	if( parseFloat($(this).val()) > parseFloat(data_validation.maximum_amount_items_billing) ){
		if(!confirm("La factura ha superado la Cantidad Maxima de " + data_validation.maximum_amount_items_billing + ", ¿Desea Continuar?")){
			$(this).val("").focus()
		}
	}
})

$("[name=vttotal]").change(function(){
	/*
		vttotal: valor total de la factura

		Validacion
		Valida si el valor total de la factura es mayor a la valor total maximo parametrizado, pregunta si se desa continuar o no
		Recalcula el valor del cambio
	*/
	if( parseFloat($(this).custom_format_val()) > parseFloat(data_validation.top_sales_invoice) ){
		if(!confirm("La factura ha superado el Valor Total maximo de " + data_validation.top_sales_invoice + ", ¿Desea Continuar?")){
			$(this).val("")
			$("[name=canti]").focus()
		}
	}

	if( parseFloat($(this).custom_format_val()) > parseFloat($("[name=ventre]").val()) ){
		$("[name=ventre]").val($(this)).trigger("change")
	}
	calcular_valor_cambio()

	//set_pago_completo_efectivo()
	/*var medios_pagos = get_data_list("#list_medios_pago")
	if(medios_pagos.some(function(e){return e.cmpago == data_validation.medios_pago.MEDIO_PAGO_EFECTIVO})){
		var sum_medios_pagos_no_efectivo = medios_pagos
			.filter(
				function(e){
					return e.cmpago != data_validation.medios_pago.MEDIO_PAGO_EFECTIVO
				}
			).reduce(function(a,b){
				return a.vmpago + b.vmpago;
				
			}, {vmpago:0});
		var nuevo_vmpago_efectivo = $("[name=vttotal]").custom_format_val() - sum_medios_pagos_no_efectivo.vmpago
		var format_nuevo_vmpago_efectivo = currencyFormat.format(nuevo_vmpago_efectivo.toString())

		$("#list_medios_pago")
			.find("[data-name=cmpago][data-value=1000]")
			.closest("tr")
			.find("[data-name=vmpago]")
			.attr("data-value",format_nuevo_vmpago_efectivo)
			.html(format_nuevo_vmpago_efectivo)
	
	}*/

})

$("#form_deta_movement [name=pordes]").change(function(){
	/*
		pordes: porcentaje de descuento para el articulo actual

		Validacion
		Valida si el porcentaje de descuento del articulo es mayor a la porcentaje maximo parametrizado, pregunta si se desa continuar o no
		Recalcula el valor unitario del articulo actual
	*/
	if( parseFloat($(this).val()) > parseFloat(data_validation.top_discount_bills) ){
		$(this).val("").focus()
		alert(text_message_tope_descuento)
	}
	calcular_valor_unitario()
})

$("#form_deta_movement [name=vunita]").change(function(){
	/*
		vunita: valor unitario del articulo actual

		Validacion
		Valida si el valor unitario del producto es menor al precio de venta menor del articulo, pregunta si desea continuar o no
	*/
	if( parseFloat($(this).custom_format_val()) < parseFloat(pvta_menor) ){
		if(!confirm("El precio Unitario es menor al precio de Venta, ¿Desea Continuar?")){
			$(this).val("").focus()
		}
	}
})

$("#item_medio_pago [name=cmpago]").change(function(e){
	/*
		cmpago: Medio de pago para el valor de la factura
		docmpago: documento del medio de pago
		banmpago : banco del medio de pago

		Validacion
		si el medio de pago no requiere documento(docmpago) y banco(banmpago) , desabilita y envia los valores por defecto para "docmpago", "banmpago"
		en caso contrario habilita y agrega el atributo "required" a los campos
	*/
	if(this.value != ''){
		$.post('/api/get-object/',JSON.stringify({'model': 32, 'field': this.name, 'value': this.value}),function(response){
			var object = JSON.parse(response.object)[0]
			if(object.fields['ifdoc']){
				$("[name=docmpago],[name=banmpago]")
					.prop("disabled",false)
					.prop("required",true)
					.val("")
			}else{
				$("[name=docmpago]")
					.prop("disabled",true)
					.prop("required",false)
					.val("0")
				$("[name=banmpago]")
					.prop("disabled",true)
					.prop("required",false)
					.val(data_validation.medios_pago.DEFAULT_BANCO)
			}
		})
	}
})
/* Validaciones */

$("#print_bill").click(function(){
	/*
		Ejecuta la funcion para imprimir la factura actual
	*/
	print_bill($("#id_cfac").val())
})

$(window).keydown(function(event) {
	/*
		Escucha la combinacion de teclado Alt + t para mostar la ventana modal de totalizar(medios de pagos)
	*/
	if(event.altKey && event.keyCode == 84) {
		event.preventDefault();
		show_modal_totalizar()
	}
})

$('#id_carlos').change(function(){
	$("#form_deta_movement [type=submit]").prop("disabled",true)
	/*
		Eschuca el cambio en el cambio #id_carlos
		Al cambiar el #id_carlos realiza una peticion a url'api-get-object' para buscar al articulos con ese 'carlos', si no se encuentra ningun articulo con ese 'carlos' se realiza otra peticion con 'cbarras'. Esta retorna el objeto de la DB en json y se asigna a current_arlo
		Se ejecuta la funcion 'setValueFieldArlo' para enviar valores a los campos '[name=vunita],[name=name__carlos],[name=civa]' articulo del articulo
		Si no se encuentra ningun articulo se muestra un mensaje
	*/
	var input_value = this.value
	if(!input_value){
		current_arlo = null
		setValueFieldArlo()
		return
	}
	if(!current_tercero){
		current_arlo = null
		setValueFieldArlo()
		alert(text_message_seleccione_tercero)
		return
	}

	var arlo_in_list = false

	$("#list_items_mdeta tbody tr").toArray().forEach(function (e,i,a){
		var td = $(e).find("[data-name=carlos]")
		if(td.data("value") == input_value){
			$(e).find(".fa.fa-edit").click()
			arlo_in_list = true
		}
	})
	if(!arlo_in_list){
		loading_animation("Cargando Datos")
		$.post('/api/get-object/',JSON.stringify({'model': 5,'field': this.name,'value': input_value}),function(response){
			$(".animation").empty()
			if(response.object){
				var object = JSON.parse(response.object)[0]
				fields = object.fields
				current_arlo = fields
				pvta_menor = mostrar_modal_lista_precios(true)

				setValueFieldArlo()

				$("#form_deta_movement [type=submit]").prop("disabled",false)
			}else{
				current_arlo = null
				$.post('/api/get-object/',JSON.stringify({'model': 5,'field': "cbarras",'value': input_value}),function(response){
					if(response.object){
						var object = JSON.parse(response.object)[0]
						fields = object.fields
						current_arlo = fields
						pvta_menor = mostrar_modal_lista_precios(true)
					}else{
						$('#id_carlos').val("").focus()
						tooltipBootstrap($('#id_carlos'),".input-group","Este Articulo no se encuentra registrado.")
						current_arlo = null
					}
					setValueFieldArlo()
					$("#form_deta_movement [type=submit]").prop("disabled",false)
				})
			}
		})
	}else{
		$("#form_deta_movement [type=submit]").prop("disabled",false)
		calcular_total()
	}
});

$('#id_citerce').change(function(){
	/*
		Eschuca el cambio en el cambio #id_citerce
		Al cambiar el #id_citerce realiza una peticion a url'api-get-object' para buscar al tercero con ese id. Esta retorna el objeto de la DB en json y se asigna a current_tercero
		Se ejecuta la funcion 'setValueFieldTerce' para enviar valores al campo '[name=name__citerce]' del nombre del tercero
		Si no se encuentra ningun tercero se muestra un mensaje
	*/
	var input_value = this.value
	current_tercero = null

	if(!input_value){
		setValueFieldTerce()
		return
	}
	loading_animation("Cargando Datos")
	$.post('/api/get-object/',JSON.stringify({'model': 29,'field': this.name,'value': this.value}),function(response){
		$(".animation").empty()
		if(response.object){
			var object = JSON.parse(response.object)[0]
			fields = object.fields
			current_tercero = fields
		}else{
			current_tercero = null
			tooltipBootstrap($('#id_citerce'),".form-group","Esta Idendificación no se encuentra registrada.")
		}
		setValueFieldTerce()
	})
});

/*Falta por Documentar */


$("#form_medios_pago").submit(function (event){
	event.preventDefault()
	var nuevo_valor_medios_pagos = parseFloat(currencyFormat.sToN($("#form_medios_pago").find("[name=vmpago]").val()))
	if(nuevo_valor_medios_pagos <= 0){
		alert(text_message_menor_igual_cero)
		return
	}

	var total_meidos_pagos_existentes = 0
	$("#list_medios_pago tbody tr").toArray().forEach(function(e,i,a){
		var vtemp = parseFloat(currencyFormat.sToN($(e).find("[data-name=vmpago]").data("value")))
		total_meidos_pagos_existentes += vtemp
	})
	var t_temp = nuevo_valor_medios_pagos + total_meidos_pagos_existentes
	if( t_temp > parseFloat(currencyFormat.sToN($("[name=vttotal]").val()) )){
		alert(text_message_vpago_mayor_vttotal)
		return
	}

	if(customValidationInput("#item_medio_pago").valid){
		var tr = $("<tr>")
		$("#item_medio_pago")
		.find("input,select")
		.toArray()
		.forEach(function(e,i){
			var oth = $(e).closest("th")

			var value = e.value
			var data_value = e.value

			var css_class = ""

			if($(e).hasClass("input-currency")){
				//var value = currencyFormat.format(e.value)
				css_class = "value-currency"
			}

			if(e instanceof HTMLSelectElement){
				var value = $(e).find("option[value=" + e.value + "]").html()
			}
			/*if(e.name == 'vmpago'){
				value = parseFloat(e.value).format(2)
			}*/
			tr.append($("<td>",{
				"data-name":e.name,
				"data-value":data_value,
				"class":css_class,
				html:value}))
		})
		td = $("<td>")
		var btnEdit = td.append($("<button class='btn btn-info' title='Editar Registro' id='edit-item-medios-pagos' style='margin-right: 3px;'><i class='fa fa-edit'></button>"))
		var btnDelete = td.append($("<button class='btn btn-danger' title='Borrar Registro' id='delete-item-fac'><i class='fa fa-remove'></button>"))
		tr.append(btnEdit,btnDelete)
		$("#list_medios_pago").find("tbody").append(tr)

		$("#item_medio_pago").find("input,select").val("")
		$("#item_medio_pago").find("[name=canti]").val(1)
		var it = 1
		$("#list_medios_pago").find("[data-name=it]").toArray().forEach(
			function(e){
				$(e).html(it);
				$(e).attr("data-value",it);
				it++
			})
		//calcular_total()
	}
})

//function edit_item_meidos_pagos(){
$(document).on('click', '#edit-item-medios-pagos', function(){
	var target = $(this)
	parent = target.closest("tr")
	parent.find("[data-name]").each(function(i,e){

		var td = $(e)

		var input = $("#item_medio_pago").find("[name = " + td.data("name") + "]")
		input.val(td.data("value")).change()
	})
	parent.remove()
})

//function edit_item_mdeta(){
$(document).on('click', '#edit-item-fac', function(){
	var target = $(this)
	parent = target.closest("tr")
	parent.find("[data-name]").each(function(i,e){

		var td = $(e)

		var input = $("#item_mdeta").find("[name = " + td.data("name") + "]")
		input.val(td.data("value"))
		/*No lanzar el evento trigger sobre 'input', pues este vuelve a ejecutar esta funcion*/
		if(input.attr("name") != "carlos"){
			input.change()
		}
		if(input.attr("name") == "civa"){
			$("#id_civa").children("option[text='" + td.data("value") + "']").attr("selected", true);
		}
	})
	parent.remove()
});

$(document).on('click', '#delete-item-fac', function(){
	//function delete_item_mdeta(){

	$(this).closest("tr").remove()
	calcular_total()
});

$("#form_deta_movement").submit(function(event){
	event.preventDefault()

	var number_items_billing = $("#list_items_mdeta tbody tr").length

	if(number_items_billing >= data_validation.maximum_number_items_billing){
		return alert(text_message_numero_maximo_items_por_factura)
	}
	if( parseFloat($('#item_mdeta input[name=vtotal]').custom_format_val()) <= 0){
		return alert(text_message_vttotal_mayor_cero)
	}
	if(customValidationInput("#item_mdeta").valid){
		var tr = $("<tr>")
		$('#item_mdeta')
		.find("input,select")
		.toArray()
		.forEach(function(e,i){
			var oth = $(e).closest("th")

			var value = e.value
			var data_value = e.value
			var css_class = ""


			//if(eval($(e).data("if-currency"))){
			if($(e).hasClass("input-currency")) {
				//var value = currencyFormat.format(e.value)
				css_class = "value-currency"
			}

			if(e instanceof HTMLSelectElement){
				var value = $(e).find("option[value=" + e.value + "]").html()
			}
			/*if(e.name == 'vunita' || e.name == 'vtotal'){
				value = parseFloat(e.value).format(2)
			}*/
			if(e.name == "pordes"){
				if(!data_validation.discount_percentages_allow_billing) css_class += " nopadding"
			}
			if(e.type == "hidden"){
				value = ""
			}
			tr.append($("<td>",{
				"data-name":e.name,
				"data-value":data_value,
				"class":css_class,
				html:value}))
		})
		td = $("<td width='100px'>")
		var btnEdit = td.append($("<button class='btn btn-info' title='Editar Registro' id='edit-item-fac' style='margin-right: 3px;'><i class='fa fa-edit'></button>"))
		var btnDelete = td.append($("<button class='btn btn-danger' title='Borrar Registro' id='delete-item-fac'><i class='fa fa-remove'></button>"))
		tr.append(btnEdit,btnDelete)
		$("#list_items_mdeta").find("tbody").append(tr)

		$('#item_mdeta').find("input,select").val("")
		$('#item_mdeta').find("[name=canti]").val(1)
		$('#item_mdeta').find("[name=pordes]").val(0)
		/*
		$("#list_items_mdeta").find("[data-name=itfac]").toArray().forEach(
			function(e){
				$(e).html(it);
				$(e).attr("data-value",it);
			})
		*/
		it++
		calcular_total()
		var totales = calcular_vtbase_vtiva()
		$('#id_itfac').val(it)
		$("[name=vtiva]").val(Math.round(totales.vtiva)).trigger("change")
		$("[name=vtbase]").val(Math.round(totales.vtbase)).trigger("change")

		$("[name=carlos]").focus()
	}
});


function reset_form_fac(){
	$("form :input, button").prop("disabled",false);
	if(mode_view != "edit"){
		borrar_medios_pago_registrados();
		borrar_articulos_registrados();
		$("#collapse_docs > .panel-body").empty()
		$("form").trigger("reset");
		$(".date").each(function(i,e){$(e).data("DateTimePicker").date(date_appen);});
	}
}

$("#btn-save").click(function(event){

	event.preventDefault();

	if(!customValidationInput("#form_movement").valid) return
	if(!customValidationInput("#form_totales").valid) return

	if($("[name=ctifopa]").val() == data_validation.formas_pago.FORMA_PAGO_CONTADO){
		if(tot_medios_pagos < parseFloat($("[name=vttotal]").custom_format_val())){
			if(confirm("La factura actual es de tipo C|ONTADO, y el valor que pago es menor al total. ¿Dese cambiarla a CREDITO?")){
				$("[name=ctifopa]").val(data_validation.formas_pago.FORMA_PAGO_CREDITO)
			}else{
				alert(text_message_vpago_menor_vttotal)
				return
			}
		}
	}

	/*var querystring = $("form:not(#form_deta_movement)").serialize();
	var data = JSON.parse('{"' + decodeURI(querystring).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}')*/
	var data = {}
	$("form:not(#form_deta_movement) :input").toArray().forEach(function(e,i){
		if(e.name != ""){
			if($(e).hasClass("input-currency")){
				data[e.name] = currencyFormat.sToN(e.value)
			}else{
				data[e.name] = e.value
			}
		}
	})

	data.descri = data.descri.replace(/\+/g," ")

	var array_mvdeta = get_data_list("#list_items_mdeta")
	var array_medios_pagos = get_data_list("#list_medios_pago")

	var tot_medios_pagos = 0
	array_medios_pagos.forEach(function(e){tot_medios_pagos+=e.vmpago})


	if(array_medios_pagos.length){
		data.medios_pagos = array_medios_pagos
	}else{
		if($("[name=ctifopa]").val() != data_validation.formas_pago.FORMA_PAGO_CONTADO){
			data.medios_pagos = []
		}else{
			var message = alertBootstrap(text_message_ingrese_medios_pago,"warning")
			$("#form_totales").prepend(message)
			return
		}
	}
	if(array_mvdeta.length){
		data.mvdeta = array_mvdeta
	}else{
		var message = alertBootstrap(text_message_ingrese_articulos,"warning")
		containerMessages.prepend(message)
		return
	}
	loading_animation("Guardando Movimiento.")

	console.info(data)

	$.ajax({
		url: var_template_django_url,
		type: 'POST',
		data: JSON.stringify(data),
		contentType: "application/json",
		error: function(response){
			var message = alertBootstrap(text_message_error_request,"danger")
			containerMessages.prepend(message)
			$(".animation").empty()
		},
		success: function(response){
			related_information = response.related_information
			$(".animation").empty()
			if(response.error){
				var message = alertBootstrap(response.message,"danger")
			}else{
				if(mode_view != "edit"){
					//$("[name*=cmv]").val(response.cmv)
				}
				var message = alertBootstrap(response.message,"success")
			}
			
			containerMessages.prepend(message)
			console.log(response)
			if(confirm("Desea Imprimir La Factura")){
				print_bill(related_information.fields.cfac)
			}

			$("form :input, button:not(#bnt-new-fac)").prop("disabled",true).off("submit")

			$("#collapse_docs > .panel-body").empty().html(response.html)

		}
	});
	$("#medios_pago").modal("hide");
});

/*Para metros de validacion para la facturacion*/

var valores_iva = {
	1:0,
	2:8,
	3:10,
	4:16,
	5:0
};
$(document).ready(function(e){
	td_js_facdeta.forEach(function(object){
		$("#item_mdeta").find("#id_carlos").val(object.fields.carlos);
		$("#item_mdeta").find("#id_itfac").val(object.fields.itfac);
		$("#item_mdeta").find("#name__carlos").val(object.fields.nlargo);
		$("#item_mdeta").find("#id_canti").val(object.fields.canti);
		$("#item_mdeta").find("#id_pordes").val(object.fields.pordes);
		$("#item_mdeta").find("#id_civa").val(object.fields.civa);
		$("#item_mdeta").find("#id_vunita").val(currencyFormat.format(object.fields.vunita)).trigger("change");
		$("#item_mdeta").find("#id_vtotal").val(currencyFormat.format(object.fields.vtotal)).trigger("change");
		$("#form_deta_movement").submit();
		$("#form_deta_movement").trigger("reset");
		calcular_total();
	});
	td_js_facpagos.forEach(function(object){
		$("#item_medio_pago").find("#id_it").val(object.fields.it);
		$("#item_medio_pago").find("#id_cmpago").val(object.fields.cmpago);
		$("#item_medio_pago").find("#id_docmpago").val(object.fields.docmpago);
		$("#item_medio_pago").find("#id_banmpago").val(object.fields.banmpago);
		$("#item_medio_pago").find("#id_vmpago").val(currencyFormat.format(object.fields.vmpago));
		$("#item_medio_pago").submit();
		$("#item_medio_pago").trigger("reset");
	})
	if (var_template_django_is_fac_anulada){
		$("form :input, button").prop("disabled",true).off("submit");
		$("#id_cfac").addClass("cesdo-2");
	}
})

/* Da formato de fecha a los campos con la clase .date - Libreria*/
$(".date").datetimepicker({
	format: "YYYY-MM-D",
	defaultDate:date_appen
});


/* Reinicia el formulario de medios de pagos al cerra la ventana modal del mismo*/
$("#medios_pago").on("hidden.bs.modal", function () {$("#form_medios_pago").trigger("reset");});

/* Envia el Foco al vr entregado al abrir el modal de totalizar*/
$("#medios_pago").on("shown.bs.modal", function () { $(selector_element_focus_on_totalizar).focus();});

/* Expande el tab de acordeaon del encabezado de la factura para poder mostrar el modal de la descripcion */
$('#modal_descripcion').on('show.bs.modal', function (e) {
	$("#collapse_head").collapse("show")
})

/* Ejecuta el evento change del campo de seleccion del tercero*/
$("#id_citerce").change();

/*Al doble click en el vt medio pago se actualiza con el valor total de la factura*/
$("#id_vmpago").dblclick(function(){$(this).val($("#id_vttotal").val()).trigger("change");});
