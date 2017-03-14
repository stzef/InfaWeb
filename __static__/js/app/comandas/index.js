var cmesa_activa = null

function accion_mesa(div,event){
	cmesa_activa = $(div).data("cmesa")
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
	$("#modal_accion_resumen").find(".label_nmesa_modal").html(mesa.fields.nmesa)
	$("#modal_accion_resumen").find(".modal-body").empty()
	$("#modal_accion_resumen").find("#label_nmesa").html(mesa.fields.nmesa)
	$("#modal_accion_resumen").find("#label_nmero").html()
	$("#modal_accion_resumen").find("#label_fecha").html()

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
								.set("__nmenu__",detalle.fields.cmenu.nmenu)
								.set("__canti__",detalle.fields.canti)
								.set("__vunita__",detalle.fields.vunita)
								.set("__ccoda__",comanda.fields.ccoda)
							)
						)
					})
				})
			})
			div.append(table)
			$("#modal_accion_resumen").find(".modal-body").append(div)
		}else{
			alertBootstrap("Esta Mesa no tiene Comandas Actuales","info",".content")
		}

	})
}

function abrir_modal_facturar_pedido(mesa){
	$("#modal_accion_facturar").find(".label_nmesa_modal").html(mesa.fields.nmesa)
	$("#modal_accion_facturar").modal("show")
}

function abrir_modal_unir_cuentas(mesa){
	$("[id*=cuenta_]").prop("checked",false)
	$("[id*=cuenta_]").closest(".form-group").show()
	$("[id=cuenta_"+cmesa_activa+"]").closest(".form-group").hide()
	$("#modal_unir_cuenta").modal("show")
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
				console.log(response)
				$("container-mesas").empty()
				$("#modal_unir_cuenta").modal("hide")
				$("container-mesas").html(response.html)
			}
		})
	}else{
		alertBootstrap("Seleccion Las mesas a Unir","info","#modal_unir_cuenta .modal-header")
	}
}

function imprimir_resumen_pedido(cresupedi){
	var url = "/orders/print?cresupedi=_cresupedi_".set("_cresupedi_",cresupedi)
	win = window.open(url)
}

function mostrar_resumen_pedido(){
	$("#modal_accion_resumen").modal("hide")
	$("#modal_formas_pago").modal("show")
}

function resumen_pedido(){
	//$("#modal_formas_pago").modal("hide")
	WaitDialog.show("Generando Resumen de Pedido...")
	$.ajax({
		url : "/orders/summary/save/",
		type : "POST",
		data : JSON.stringify( { cmesa : cmesa_activa, medios_pago: get_medios_pago() } ),
		success : function ( response ){
			WaitDialog.hide()
			$("[data-cmesa="+cmesa_activa+"]").removeClass("activa")
			$("[data-cmesa="+cmesa_activa+"]").find("#menu_vtotal").html("$ 0")
			$("[data-cmesa="+cmesa_activa+"]").find("#mesa_mesero").html("-")
			$("#modal_accion_resumen").modal("hide")
			alertBootstrap("El Resumen de Pedido se Guardo","success",".content")
			imprimir_resumen_pedido(response.pk)
		}
	})
}

function facturar_pedido(){
	$("#modal_accion_facturar").modal("hide")
}

function get_medios_pago(){
	return $("#example").find("tbody tr[role=row]").toArray().map(function(row){
		data = {}
		$(row).find("input,select").toArray().forEach(function(input){
			data[input.name] = input.value
		})
		return data
	})
}

function verificar_total_pago(){

	var data = get_medios_pago()
	console.warn(data)
	var totales = data.map(function(row){return parseFloat(row.vmpago)})
	var totales = totales.reduce(function(a,b){ return a + b },0)

	WaitDialog.show("Procesando...")
	$.ajax({
		url:"/tables/info-sumary/__cmesa__/".set("__cmesa__",cmesa_activa),
		type:"POST",
		success:function(response){
			WaitDialog.hide()
			if( totales > response.vttotal ){
				alertBootstrap("El Valor No debe superar el saldo de la mesa","info",".content")
			}
		}
	})

	console.info(totales)
}

$('#modal_accion_mesa,#modal_accion_resumen,#modal_accion_facturar,#modal_unir_cuenta').on('hidden.bs.modal', function () {
	cmesa_activa = null
})
$('#modal_accion_resumen,#modal_accion_facturar,#modal_formas_pago,#modal_unir_cuenta').on('shown.bs.modal', function() {
	cmesa_activa = parseInt($("#modal_input_mesa_activa").val())
})

var editor = new $.fn.dataTable.Editor( {
	table: "#example",
	ajax : false,
	i18n: CONF_DTE.i18n,
	fields: [
		{label: "Item:",name:  "medios_pago.it","type" : "hidden"},
		{label: "Codigo:",name:  "medios_pago.cmpago"},
		{label: "Ingrediente:",name:  "medios_pago.docmpago",type: "text"},
		{label: "Cantidad:",name:  "medios_pago.banmpago",type: "text"},
		{label: "Vr Total:",name:  "medios_pago.vmpago",type: "text"}
	]
})

editor.on("create remove",function(event, response, data){
	verificar_total_pago()
})

var table_crud = $('#example').DataTable( {
	dom: "Bfrtip",
	ajax: false,
	columns: [
		{ data: "medios_pago.it" },
		{ data: "medios_pago.cmpago" },
		{ data: "medios_pago.docmpago" },
		{ data: "medios_pago.banmpago" },
		{ data: "medios_pago.vmpago" }
	],
	select: 'single',
	buttons: [
		{ editor: editor,className:CONF_DTE.buttons.create.className, text:CONF_DTE.buttons.create.text, action: function ( e, dt, node, config ) {
			console.log("agregar")
			table_crud.row.add({DT_RowId:"row_1",medios_pago:{
				it:$("#template_it").html(),cmpago:$("#template_cmpago").html(),docmpago:$("#template_docmpago").html(),banmpago:$("#template_banmpago").html(),vmpago:$("#template_vmpago").html()}
			}).draw(false)
			verificar_total_pago()
		}},
		{ extend: "remove", editor: editor,className:CONF_DTE.buttons.remove.className, text:CONF_DTE.buttons.remove.text}
	],
	language: CONF_DTE.language
})
