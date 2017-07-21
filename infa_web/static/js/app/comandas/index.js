var cmesa_activa = null

$(document).ready(function() {

	WaitDialog.show("Cargando...")
	$.ajax({
		type  : "GET",
		url : "/general/defaults",
		success: function(data){
			WaitDialog.hide()
			appem_defaults = data
		},
		error : function(data){
			WaitDialog.hide()
			WaitDialog.show("Ocurrio Un Error el la Carga")
		}
	})
})

function accion_mesa(div,event){
	cmesa_activa = $(div).data("cmesa")
	nmesa_activa = $(div).data("nmesa")
	$("#modal_accion_mesa").find(".label_nmesa_modal").html(nmesa_activa)

	$("#modal_input_mesa_activa").val(cmesa_activa)
	$("#modal_accion_mesa").modal("show")
}

function realizar_accion(button,event){
	Models.objects.findOne("Mesas",{cmesa : cmesa_activa},function(error,mesa){
		if( $(button).data("value") == "R" ) abrir_modal_resumen_pedido(mesa)
		// if( $(button).data("value") == "F" ) abrir_modal_facturar_pedido(mesa)
		if( $(button).data("value") == "UC" ) abrir_modal_unir_cuentas(mesa)
		if( $(button).data("value") == "PA" ) abrir_modal_listado_pedidos(mesa)
		$("#modal_accion_mesa").modal("hide")
	})
}

function abrir_modal_resumen_pedido(mesa){
	$("#modal_accion_resumen #btn_pagar_pedido").removeClass("hide")

	var div_mesa = $(".mesa[data-cmesa=__cmesa__]".set("__cmesa__",cmesa_activa))

	$("#modal_accion_resumen").find(".label_vtotal_mesa_modal").html( currencyFormat.format( div_mesa.data("vttotal") ) )

	$("#modal_accion_resumen").find(".label_nmesa_modal").html(mesa.fields.nmesa)
	$("#modal_accion_resumen").find("#section-detalle-comanda").empty()
	$("#modal_accion_resumen").find("#label_nmesa").html(mesa.fields.nmesa)

	Models.objects.find("Coda",{cmesa : cmesa_activa, cresupedi:"__NULL__",cesdo__cesdo:1},function(error,comandas){
		console.info(comandas)
		if ( comandas ) {
			$("#modal_accion_resumen").modal("show")
			var div = $("<div></div>")
			var template_thead = "<table class='table table-striped'>"+
				"<thead>"+
					"<tr>"+
						"<th>Comanda</th>"+
						"<th>Menu</th>"+
						"<th>Cantidad</th>"+
						"<th>Vr. Unitario</th>"+
					"</tr>"+
				"</thead>"+
			"</table>"
			var table = $(template_thead)
			comandas.forEach(function(comanda){
				Models.objects.find("Codadeta",{ccoda__ccoda:comanda.fields.ccoda},function(error,detalles){
					console.warn(detalles)
					if ( detalles ){
						detalles.forEach(function(detalle){
							var template_tr = "<tr>"+
								"<td>Comanda # __ccoda__</td>"+
								"<td>__nmenu__</td>"+
								"<td>__canti__</td>"+
								"<td>__vunita__</td>"+
							"</tr>"
							table.append(
								$(template_tr
									.set("__ccoda__",comanda.fields.ccoda)
									.set("__nmenu__",detalle.fields.cmenu.ncorto)
									.set("__canti__",detalle.fields.canti)
									.set("__vunita__", currencyFormat.format(detalle.fields.vunita))
								)
							)
						})
					}
				})
			})
			div.append(table)
			$("#modal_accion_resumen").find("#section-detalle-comanda").append(div)
		}else{
			alertify.warning("Esta mesa no tiene comandas actuales")
		}

	})
}

/*
function abrir_modal_facturar_pedido(mesa){
	$("#modal_accion_facturar").find(".label_nmesa_modal").html(mesa.fields.nmesa)
	$("#modal_accion_facturar").modal("show")
}
*/

function abrir_modal_unir_cuentas(mesa){
	var selector = ".mesa.activa:not([data-cmesa=__cmesa__])".set("__cmesa__",cmesa_activa)
	meses_unificables = $(selector)
	console.info(meses_unificables)

	if ( meses_unificables.length >= 1 ){
		$("#modal_unir_cuenta").modal("show")
		meses_unificables.toArray().forEach(function(mesa){

			var div_mesa = $(".mesa[data-cmesa=__cmesa__]".set("__cmesa__",$(mesa).data("cmesa")))

			var t = '<div class="form-group container_cuenta___cmesa__">'+
						'<label class="btn btn-primary" for="cuenta___cmesa__">'+
							'<input type="checkbox" id="cuenta___cmesa__" value="__cmesa__">'+
							'<p>__nmesa__</p>'+
							'<p>__vttotal__</p>'+
						'</label>'+
					'</div>'
			t = t.set("__cmesa__",div_mesa.data("cmesa")).set("__nmesa__",div_mesa.data("nmesa")).set("__vttotal__",div_mesa.data("vttotal"))
			$("#modal_unir_cuenta .modal-body").append($(t))
		})

		$("#modal_unir_cuenta").find(".label_nmesa_modal").html(mesa.fields.nmesa)
		$("[id*=cuenta_]").prop("checked",false)
		$("[id*=cuenta_]").closest(".form-group").show()

		$("[id=cuenta_"+cmesa_activa+"]").closest(".form-group").hide()
	}else{
		alertify.warning("No hay mesas para unir");
	}

}

function abrir_modal_listado_pedidos(mesa){
	console.log(mesa)
	$("#modal_listado_pedidos").modal("show")
	var cmesa = mesa.pk
	$.ajax({
		url : `/tables/info-resupedi/${cmesa}/`,
		type : "POST",
		dataType : "json",
		success : function(response){
			table_resupedi.rows().remove().draw(false)
			response.forEach( resupedi => {
				table_resupedi.rows.add([
					{
						resupedi: {
							credupedi: resupedi.pk,
							vttotal: currencyFormat.format(resupedi.fields.vttotal),
							btn_fac: `<button class='btn btn-info' onclick="facturar_pedido(${resupedi.pk})">Facturar</button>`,
							btn_print: `<a class='btn btn-info' target='_blank' href='/orders/print/?cresupedi=${resupedi.pk}'>Imprimir</a>`
						}
					}
				]).draw(false)
			} )
		}
	})
}

function unir_cuentas(){
	var mesas = $("#modal_unir_cuenta").find("input:checked")
	var cmesas = mesas.toArray().map(function(mesa){return mesa.value})

	if( mesas.length != 0 ){
		WaitDialog.show("Uniendo Cuentas...")
		$.ajax({
			url : "/orders/join/",
			type : "POST",
			data : JSON.stringify( { mesa : cmesa_activa , mesas : cmesas } ),
			success : function ( response ){
				WaitDialog.hide()
				$("container-mesas").empty()
				$("#modal_unir_cuenta").modal("hide")
				$(".container-mesas").html(response.html)
			}
		})
	}else{
		alertify.warning("Seleccion las mesas a unir")
	}
}

function imprimir_resumen_pedido(cresupedi){
	var url = "/orders/print?cresupedi=_cresupedi_".set("_cresupedi_",cresupedi)
	win = window.open(url)
}
function resumen_pedido(){

	var ok_formas_pago = verificar_total_pago()
	var ok_form_formas_pago = customValidationInput($("#modal_accion_resumen table tbody")).valid
	if ( ok_formas_pago && ok_form_formas_pago ){
		var data_save = { cmesa : cmesa_activa, medios_pago: get_medios_pago() }
		if( data_save.medios_pago.length == 0){
			return alertify.warning("Seleccione por lo menos un medio de Pago")
		}
		WaitDialog.show("Generando Resumen de Pedido...")
		$.ajax({
			url : "/orders/summary/save/",
			type : "POST",
			dataType : 'json',
			data : JSON.stringify( data_save ),
			success : function ( response ){
				imprimir_resumen_pedido(response.resupedi.pk)
				WaitDialog.hide()
				$("[data-cmesa="+cmesa_activa+"]").removeClass("activa")
				$("[data-cmesa="+cmesa_activa+"]").find("#menu_vtotal").html("$ 0")
				$("[data-cmesa="+cmesa_activa+"]").find("#mesa_mesero").html("-")

				$("#modal_unir_cuenta").find(".container_cuenta___cmesa__".set("__cmesa__",cmesa_activa)).remove()
				$("#modal_accion_resumen #btn_pagar_pedido").addClass("hide")
				$("#modal_accion_resumen #btn_facturar_pedido").attr("data-cresupedi",response.resupedi.pk)
				// $("#modal_accion_resumen").modal("hide")

				alertify.success("El resumen de pedido se guardo.")

				table_crud.rows().remove().draw()
			}
		})
	}
}
function print_bill(cfac){
	/*
		@param cfac String : codigo de factura a imprimir
		Abre una nueva ventana con la factura en pdf
	*/
	window.open("/pos/print?cfac=" + cfac)
}
function facturar_pedido(cresupedi){
	console.log('Facturando... ' + cresupedi)

	Models.objects.findOne("Resupedi",{cresupedi : cresupedi},function(error,resupedi){
		console.log(resupedi)
		if ( resupedi ){
			Models.objects.find("Coda",{cresupedi__cresupedi : resupedi.pk},function(error,comandas){
				console.log(comandas)
				var ccodas = comandas.map( comanda => comanda.fields.ccoda )
				console.log(ccodas)
				Models.objects.find("Codadeta",{ccoda__ccoda : ccodas[0]},function(error,detalles){
					console.info(detalles)


					var vttotal = resupedi.fields.vttotal

					var data = {
						//"mode_view":"create",
						"citerce":appem_defaults.tercero.pk,
						"name__citerce":appem_defaults.tercero.fields.nomcomer,
						"cvende":appem_defaults.current_vendedor.pk,
						"cdomici":appem_defaults.domiciliario.pk,
						"ctifopa":appem_defaults.forma_pago.pk,
						"femi":moment().format("YYYY-MM-DD"),
						"fpago":moment().format("YYYY-MM-DD"),
						"cemdor":appem_defaults.empacador.pk,
						"ccaja":appem_defaults.current_user_appem.fields.ccaja,
						"cesdo":appem_defaults.estado.pk,
						"descri":"",
						"vttotal":vttotal,
						"ventre":vttotal,
						"vcambio":0,
						"vtbase":vttotal,
						"vtiva":0,
						"brtefte":0,
						"prtefte":0,
						"vrtefte":0,
						"vflete":0,
						"vdescu":0,
						"medios_pagos":[{
							"it":1,
							"cmpago":appem_defaults.medio_pago.pk,
							"docmpago":0,
							"banmpago":appem_defaults.banco.pk,
							"vmpago":vttotal
						}],
						"mvdeta":[]
					}
					var it = 1
					data.mvdeta = detalles.map(function(item){
						var d = {
							"itfac":it,
							"carlos":item.fields.cmenu.carlos,
							"name__carlos":item.fields.cmenu.ncorto,
							"canti":item.fields.canti,
							"pordes":0,
							"civa":1,
							"vunita":currencyFormat.sToN(item.fields.cmenu.pvta1),
							"vtotal":0
						}
						it++
						d.vtotal = d.canti * d.vunita
						return d
					})
					console.log(data)
					WaitDialog.show("Guardando")
					$.ajax({
						url: "/bill/save/",
						type: 'POST',
						data: JSON.stringify(data),
						contentType: "application/json",
						error: function(response){
							WaitDialog.hide()
							alertify.notify(response.responseJSON.message,"error")
						},
						success: function(response){
							WaitDialog.hide()
							related_information = response.related_information
							if(response.error){
								alertify.notify(response.message,"danger")
							}else{
								alertify.notify(response.message,"success")
							}
							alertify.confirm("Desea Imprimir La Factura __cfac__".set("__cfac__",related_information.fields.cfac),function(){
								print_bill(related_information.fields.cfac)
							})

						}
					});


				})
			})
		}
	})


}

function get_medios_pago(){
	return $("#example").find("tbody tr[role=row]").toArray().map(function(row){
		data = {}
		$(row).find("input,select").toArray().forEach(function(input){
			if ( $(input).hasClass("input-currency") ){
				data[input.name] = currencyFormat.sToN(input.value)
			}else{
				data[input.name] = input.value
			}
		})
		return data
	})
}

function verificar_total_pago(input,event){

	var ok = true
	var div_mesa = $(".mesa[data-cmesa=__cmesa__]".set("__cmesa__",cmesa_activa))

	var l_vttotal = parseFloat(div_mesa.data("vttotal"))
	var data = get_medios_pago()
	var totales = data.map(function(row){
		var vmpago = row.vmpago
		if ( isNaN(parseFloat(vmpago)) ){return 0}
		return parseFloat(vmpago)
	})
	var totales = totales.reduce(function(a,b){ return a + b },0)
	if( totales > l_vttotal ){
		// input.value = ""
		alertify.warning("El valor no debe superar el saldo de la mesa.")
		var ok = false
	}
	if( totales < l_vttotal ){
		alertify.warning("El valor no debe ser menor a el saldo de la mesa.")
		var ok = false
	}
	return ok
}

$('#modal_accion_mesa,#modal_accion_resumen,#modal_accion_facturar,#modal_unir_cuenta').on('hidden.bs.modal', function () {
	cmesa_activa = null
	table_crud.rows().remove().draw()
})

//$('#modal_formas_pago').on('hidden.bs.modal', function () {
$('#modal_accion_resumen').on('hidden.bs.modal', function () {
	table_crud.rows().remove().draw()
})
//$('#modal_formas_pago').on('shown.bs.modal', function () {
$('#modal_accion_resumen').on('shown.bs.modal', function () {
	// table_crud.buttons(".btn-create").trigger()
	cmesa_activa = parseInt($("#modal_input_mesa_activa").val())
	table_crud.button(".btn-create").trigger("click")

	var div_mesa = $(".mesa[data-cmesa=__cmesa__]".set("__cmesa__",cmesa_activa))
	var l_vttotal = parseFloat(div_mesa.data("vttotal"))

	$('#modal_accion_resumen').find("[name=vmpago]").val(l_vttotal).trigger("change")
	$('#modal_accion_resumen').find("[name=cmpago]").val(1000).trigger("change")
})

$('#modal_accion_facturar,#modal_formas_pago,#modal_unir_cuenta').on('shown.bs.modal', function() {
	cmesa_activa = parseInt($("#modal_input_mesa_activa").val())
})


var table_resupedi = $('#table-resupedi').DataTable( {
	language: CONF_DTE.language,
	columns: [
		{ data: "resupedi.credupedi" },
		{ data: "resupedi.vttotal" },
		{ data: "resupedi.btn_fac" },
		{ data: "resupedi.btn_print" }
	],
} )
var table_crud = $('#example').DataTable( {
	dom: "Bfrtip",
	ajax: false,
	columns: [
		{ data: "medios_pago.cmpago" },
		{ data: "medios_pago.docmpago" },
		{ data: "medios_pago.banmpago" },
		{ data: "medios_pago.vmpago" }
	],
	select: 'single',
	buttons: [
		{
			className:CONF_DTE.buttons.create.className,
			text:CONF_DTE.buttons.create.text,
			action : function ( e, dt, node, config ) {
				table_crud.row.add({
					DT_RowId:"row_1",
					medios_pago:{
						cmpago:$("#template_cmpago").html(),
						docmpago:$("#template_docmpago").html(),
						banmpago:$("#template_banmpago").html(),
						vmpago:$("#template_vmpago").html()
					}
				}).draw(false)
				$("#modal_accion_resumen #id_vmpago").inputCurrency()
				$("#modal_accion_resumen #id_cmpago").val(1000)
			}
		},
		{
			className:CONF_DTE.buttons.remove.className, text:CONF_DTE.buttons.remove.text,
			action : function(){
				table_crud.rows({selecte:true}).remove().draw()
			}
		}

	],
	language: CONF_DTE.language
})

// table_crud.button(".btn-create").trigger("click")
