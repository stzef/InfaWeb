var selector_element_focus_on_totalizar = "[name=ventre]"

var mode_view = $("#mode_view").val()
var it = 1
var vttotal_cartera_tercero = 0
var containerMessages = $("#messages-container")
$('#id_itfac').val(it)

var text_message_ingrese_medios_pago = "No ha ingresado ningún Medio de Pago."
var text_message_ingrese_articulos = "No ha ingresado ningún Artículo."
var text_message_descuento_mayor_vttotal = "No puede realizar un Descuento Mayor al Valor Total."
var text_message_error_request = "Ha ocurrido un error en el proceso."
var text_message_menor_igual_cero = "El Valor a Pagar no puede ser menor o igual a cero."
var text_message_vpago_mayor_vttotal = "El Valor a Pagar no puede ser mayor al Valor Total."

function print_rc(cmovi){
	window.open("/cartera/print?cmovi=" + cmovi)
}

function borrar_medios_pago_registrados(){
	$("#list_medios_pago").find("tbody").children().remove()
}
function borrar_articulos_registrados(){
	$("#list_items_mdeta").find("tbody").children().remove()
}

function show_modal_totalizar(){

	var array_mvdeta = get_data_list("#list_items")
	if(!array_mvdeta.length) return containerMessages.prepend(alertBootstrap(text_message_ingrese_articulos,"warning"))

	$("#medios_pago").modal("show")
	
}

function calcular_total(){
	/*
		Calcula el valor Total del Abono
		Recorre todos los items del abono calculando el valor individual y sumandolos
	*/
	var vt_vmovi = sum_cell("#form_items #list_items table","vmovi")
	
	$("[name=vttotal]").val(vt_vmovi).trigger("change")
	$("#mask_vttotal").val(vt_vmovi).trigger("change")
	$("[name=ventre]").val(vt_vmovi).trigger("change")
}

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

$('#id_citerce').change(function(){
	/*
		Eschuca el cambio en el cambio #id_citerce
		Al cambiar el #id_citerce realiza una peticion a url'api-get-object' para buscar al tercero con ese id. Esta retorna el objeto de la DB en json y se asigna a current_tercero
		Se ejecuta la funcion 'setValueFieldTerce' para enviar valores al campo '[name=name__citerce]' del nombre del tercero
		Si no se encuentra ningun tercero se muestra un mensaje
	*/
	var input_value = this.value
	current_tercero = null
	vttotal_cartera_tercero = 0

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
			var cartera = getCartera(object.pk)
			
		}else{
			current_tercero = null
			vttotal_cartera_tercero = 0
			tooltipBootstrap($('#id_citerce'),".form-group","Esta Idendificación no se encuentra registrada.")
		}
		setValueFieldTerce()
	})
});

function pintar_cartera(cartera){
	$("#cartera_tercero tbody").empty()
	cartera.cartera.forEach(function(movimiento){
		var tr = $("<tr>")
		tr.append($("<td>",{html:movimiento.pk}))
		tr.append($("<td>",{html:currencyFormat.format(movimiento.fields.vttotal)}))
		$("#cartera_tercero tbody").append(tr)
	})
}
function getCartera(citerce){
	$.get('/cartera/get_cartera/' + citerce,function(response){
		response.cartera = JSON.parse(response.cartera)
		console.info(response)
		vttotal_cartera_tercero = currencyFormat.sToN(response.vttotal)
		pintar_cartera(response)
	})
}

/*Falta por Documentar */

/*
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
		//No lanzar el evento trigger sobre 'input', pues este vuelve a ejecutar esta funcion
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
*/

function reset_form_fac(){
	$("form :input, button").prop("disabled",false);
	$("#vttotal__mask").prop("disabled",false);
	if(mode_view != "edit"){
		$("#vttotal__mask").val(0).trigger("change");
		borrar_medios_pago_registrados();
		borrar_articulos_registrados();
		$("form").trigger("reset");
		$(".date").each(function(i,e){$(e).data("DateTimePicker").date(date_appen);});
	}
	$("#collapse_head,#collapse_deta").collapse("hide")
	$("#collapse_head").collapse("show")
}

$("#btn-save").click(function(event){

	event.preventDefault();

	if(!customValidationInput("#form_movement").valid) return
	if(!customValidationInput("#form_totales").valid) return

	var array_mvdeta = get_data_list("#form_items #list_items table")
	var array_medios_pagos = get_data_list("#form_medios_pago #list_items table")

	var tot_medios_pagos = 0
	array_medios_pagos.forEach(function(e){tot_medios_pagos+=e.vmpago})



	/*var querystring = $("form:not(#form_deta_movement)").serialize();
	var data = JSON.parse('{"' + decodeURI(querystring).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g,'":"') + '"}')*/
	var data = {}
	$("form :input").toArray().forEach(function(e,i){
		if(e.name != ""){
			if($(e).hasClass("input-currency")){
				data[e.name] = currencyFormat.sToN(e.value)
			}else{
				data[e.name] = e.value
			}
		}
	})

	if(array_medios_pagos.length){
		data.mpagos = array_medios_pagos
	}else{
		var message = alertBootstrap(text_message_ingrese_medios_pago,"warning")
		$("#form_totales").prepend(message)
		return
	}
	if(array_mvdeta.length){
		data.deta = array_mvdeta
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
			if(confirm("Desea Imprimir El Recibo de Caja")){
				print_bill(related_information.fields.cfac)
			}

			$("form :input, button:not(#bnt-new-fac)").prop("disabled",true).off("submit")
		}
	});
	$("#medios_pago").modal("hide");
});

/*Para metros de validacion para la facturacion*/
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

/* Ejecuta el evento change del campo de seleccion del tercero*/
$("#id_citerce").change();

/*Al doble click en el vt medio pago se actualiza con el valor total de la factura*/
$("#id_vmpago").dblclick(function(){$(this).val($("#id_vttotal").val()).trigger("change");});

function max_value_for_item_deta(){
	var vttotal_items = sum_cell("#form_items #list_items table","vmovi")
	var vtotal_item = parseFloat($(this).find("[name=vmovi]").custom_format_val())
	var vttotal_local = vttotal_items + vtotal_item

	if(vttotal_local > vttotal_cartera_tercero) return false
	return true
}
function max_value_for_item_pago(){
	var vttotal_items = sum_cell("#form_medios_pago #list_items table","vmpago")
	var vtotal_item = parseFloat($(this).find("[name=vmpago]").custom_format_val())
	var vttotal_local = vttotal_items + vtotal_item

	if(vttotal_local > parseFloat($("[name=vttotal]").custom_format_val())) return false
	return true
}
function min_value_for_item(obj_params){
	var selector_input = "[name=" + obj_params.input_name + "]"
	var vtotal_item = parseFloat($(this).find(selector_input).custom_format_val())

	if(vtotal_item <= 0) return false
	return true
}


$("#form_items").customTable(
	[
		{fn:max_value_for_item_deta,params:{},msg:"El valor no puede superar el total"},
		{fn:min_value_for_item,params:{input_name:"vmovi"},msg:"El valor no puede se menor o igual a 0"}
	]
).on("insert_row",function(){
	console.log("insert_row")
	calcular_total()
})

$("#form_medios_pago").customTable([
		{fn:max_value_for_item_pago,params:{},msg:"El valor no puede superar el total"},
		{fn:min_value_for_item,params:{input_name:"vmpago"},msg:"El valor no puede se menor o igual a 0"}
	]
)
