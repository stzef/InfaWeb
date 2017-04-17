var cmesa_activa = null

function accion_mesa(div,event){
	cmesa_activa = $(div).data("cmesa")
	nmesa_activa = $(div).data("nmesa")
	$("#modal_accion_mesa").find(".label_nmesa_modal").html(nmesa_activa)

	$("#modal_input_mesa_activa").val(cmesa_activa)
	$("#modal_accion_mesa").modal("show")
}

function realizar_accion(div,event){
	Models.objects.findOne("Mesas",{cmesa : cmesa_activa},function(error,mesa){
		if( $("#modal_input_action").val() == "R" ) abrir_modal_resumen_pedido(mesa)
		if( $("#modal_input_action").val() == "F" ) abrir_modal_facturar_pedido(mesa)
		if( $("#modal_input_action").val() == "UC" ) abrir_modal_unir_cuentas(mesa)
		$("#modal_accion_mesa").modal("hide")
	})
}

function abrir_modal_resumen_pedido(mesa){
	console.log(mesa)

	var div_mesa = $(".mesa[data-cmesa=__cmesa__]".set("__cmesa__",cmesa_activa))

	//$("#modal_accion_resumen").find(".label_nmesa_modal").html(div_mesa.data("nmesa"))
	$("#modal_accion_resumen").find(".label_vtotal_mesa_modal").html( currencyFormat.format( div_mesa.data("vttotal") ) )

	$("#modal_accion_resumen").find(".label_nmesa_modal").html(mesa.fields.nmesa)
	$("#modal_accion_resumen").find("#section-detalle-comanda").empty()
	$("#modal_accion_resumen").find("#label_nmesa").html(mesa.fields.nmesa)

	Models.objects.find("Coda",{cmesa : cmesa_activa, cresupedi:"__NULL__",cesdo__cesdo:1},function(error,comandas){
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
				Models.objects.find("Codadeta",{ccoda:comanda.pk},function(error,detalles){
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
								.set("__nmenu__",detalle.fields.cmenu.nmenu)
								.set("__canti__",detalle.fields.canti)
								.set("__vunita__", currencyFormat.format(detalle.fields.vunita))
							)
						)
					})
				})
			})
			div.append(table)
			$("#modal_accion_resumen").find("#section-detalle-comanda").append(div)
		}else{
			//alertBootstrap("Esta Mesa no tiene Comandas Actuales","info",".content")
			alertify.warning("Esta Mesa no tiene Comandas Actuales")
		}

	})
}

function abrir_modal_facturar_pedido(mesa){
	$("#modal_accion_facturar").find(".label_nmesa_modal").html(mesa.fields.nmesa)
	$("#modal_accion_facturar").modal("show")
}

function abrir_modal_unir_cuentas(mesa){
	var selector = ".mesa.activa:not([data-cmesa=__cmesa__])".set("__cmesa__",cmesa_activa)
	meses_unificables = $(selector)

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
		//alertBootstrap("No hay mesas para unir","info",".content")
		alertify.warning("No hay mesas para unir");
	}

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
		//alertBootstrap("Seleccion Las mesas a Unir","info","#modal_unir_cuenta .modal-header")
		alertify.warning("Seleccion Las mesas a Unir")
	}
}

function imprimir_resumen_pedido(cresupedi){
	var url = "/orders/print?cresupedi=_cresupedi_".set("_cresupedi_",cresupedi)
	win = window.open(url)
}
/*
function mostrar_resumen_pedido(){
	var div_mesa = $(".mesa[data-cmesa=__cmesa__]".set("__cmesa__",cmesa_activa))

	$("#modal_formas_pago").find(".label_nmesa_modal").html(div_mesa.data("nmesa"))
	$("#modal_formas_pago").find(".label_vtotal_mesa_modal").html( currencyFormat.format( div_mesa.data("vttotal") ) )



	$("#modal_accion_resumen").modal("hide")
	$("#modal_formas_pago").modal("show")
}
*/
function resumen_pedido(){

	//$("#modal_formas_pago").modal("hide")
	var ok_formas_pago = verificar_total_pago()
	var ok_form_formas_pago = customValidationInput($("#modal_formas_pago table tbody")).valid
	if ( ok_formas_pago && ok_form_formas_pago ){
		//$("#modal_formas_pago").modal("hide")
		var data_save = { cmesa : cmesa_activa, medios_pago: get_medios_pago() }
		if( data_save.medios_pago.length == 0){
			//return alertBootstrap("Seleccione por lo menos un medio de Pago","info","#modal_formas_pago .modal-header")
			return alertify.warning("Seleccione por lo menos un medio de Pago")
		}
		WaitDialog.show("Generando Resumen de Pedido...")
		$.ajax({
			url : "/orders/summary/save/",
			type : "POST",
			data : JSON.stringify( data_save ),
			success : function ( response ){
				WaitDialog.hide()
				$("[data-cmesa="+cmesa_activa+"]").removeClass("activa")
				$("[data-cmesa="+cmesa_activa+"]").find("#menu_vtotal").html("$ 0")
				$("[data-cmesa="+cmesa_activa+"]").find("#mesa_mesero").html("-")

				$("#modal_unir_cuenta").find(".container_cuenta___cmesa__".set("__cmesa__",cmesa_activa)).remove()

				$("#modal_accion_resumen").modal("hide")
				$("#modal_formas_pago").modal("hide")

				//alertBootstrap("El Resumen de Pedido se Guardo","success",".content")
				alertify.success("El Resumen de Pedido se Guardo")

				table_crud.rows().remove().draw()

				// imprimir_resumen_pedido(response.pk)
			}
		})
	}
}

function facturar_pedido(){
	$("#modal_accion_facturar").modal("hide")
}

function get_medios_pago(){
	return $("#example").find("tbody tr[role=row]").toArray().map(function(row){
		data = {}
		$(row).find("input,select").toArray().forEach(function(input){
			if ( $(input).hasClass("input-currency") ){
				console.log(input.value)
				console.log(typeof input.value)
				data[input.name] = currencyFormat.sToN(input.value)
			}else{
				data[input.name] = input.value
			}
		})
		return data
	})
}

function verificar_total_pago(input,event){

	/*WaitDialog.show("Procesando...")
	$.ajax({
		url:"/tables/info-sumary/__cmesa__/".set("__cmesa__",cmesa_activa),
		type:"POST",
		success:function(response){
			WaitDialog.hide()
			response.vttotal = parseFloat(response.vttotal)
			var data = get_medios_pago()
			var totales = data.map(function(row){
				var vmpago = row.vmpago
				if ( isNaN(parseFloat(vmpago)) ){return 0}
				return parseFloat(vmpago)
			})
			var totales = totales.reduce(function(a,b){ return a + b },0)
			if( totales > response.vttotal ){
				input.value = ""
				alertBootstrap("El Valor No debe superar el saldo de la mesa","info","#modal_formas_pago .modal-header")
			}
			if( totales < response.vttotal ){
				alertBootstrap("El Valor No debe ser menor a el saldo de la mesa","info","#modal_formas_pago .modal-header")
			}
		}
	})*/
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
		input.value = ""
		//alertBootstrap("El Valor No debe superar el saldo de la mesa","info","#modal_formas_pago .modal-header")
		alertify.warning("El Valor No debe superar el saldo de la mesa")
		var ok = false
	}
	if( totales < l_vttotal ){
		//alertBootstrap("El Valor No debe ser menor a el saldo de la mesa","info","#modal_formas_pago .modal-header")
		alertify.warning("El Valor No debe ser menor a el saldo de la mesa")
		var ok = false
	}
	return ok

}

$('#modal_accion_mesa,#modal_accion_resumen,#modal_accion_facturar,#modal_unir_cuenta').on('hidden.bs.modal', function () {
	cmesa_activa = null
	table_crud.rows().remove().draw()
})

$('#modal_formas_pago').on('hidden.bs.modal', function () {
	table_crud.rows().remove().draw()
})
$('#modal_formas_pago').on('shown.bs.modal', function () {
	table_crud.buttons(".btn-create").trigger()
})

$('#modal_accion_resumen,#modal_accion_facturar,#modal_formas_pago,#modal_unir_cuenta').on('shown.bs.modal', function() {
	cmesa_activa = parseInt($("#modal_input_mesa_activa").val())
})

var editor = new $.fn.dataTable.Editor( {
	table: "#example",
	ajax : false,
	i18n: CONF_DTE.i18n,
	fields: [
		{label: "Codigo:",name:  "medios_pago.cmpago"},
		{label: "Ingrediente:",name:  "medios_pago.docmpago",type: "text"},
		{label: "Cantidad:",name:  "medios_pago.banmpago",type: "text"},
		{label: "Vr Total:",name:  "medios_pago.vmpago",type: "text"}
	]
})

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
		{ editor: editor,className:CONF_DTE.buttons.create.className, text:CONF_DTE.buttons.create.text, action: function ( e, dt, node, config ) {
			table_crud.row.add({
				DT_RowId:"row_1",
				medios_pago:{
					cmpago:$("#template_cmpago").html(),
					docmpago:$("#template_docmpago").html(),
					banmpago:$("#template_banmpago").html(),
					vmpago:$("#template_vmpago").html()
				}
			}).draw(false)
			$("#modal_formas_pago #id_vmpago").inputCurrency()
			$("#modal_formas_pago #id_cmpago").val(1000)
		}},
		{ extend: "remove", editor: editor,className:CONF_DTE.buttons.remove.className, text:CONF_DTE.buttons.remove.text}
	],
	language: CONF_DTE.language
})
