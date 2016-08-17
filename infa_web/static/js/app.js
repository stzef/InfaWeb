function AJAXGenericView(selectorForm,selectorInput,nField,url){
	$(selectorForm).submit(function(event){
		var currentForm = $(this)
		event.preventDefault()
		$.ajax({
			url: url,
			type: 'POST',
			data: $("form").serialize(),
			contentType: "application/x-www-form-urlencoded",
			error: function(response){
				$('<ul class="errorlist"></ul>')
				var data = JSON.parse(response.responseText)
				for (field in data.errors){
					var ul = $('<ul class="errorlist"></ul>')
					var selector = "[name=" + field + "]"
					for (var error of data.errors[field]){
						var message = alertBootstrap(error,"danger")
						ul.append($("<li>").append(message))
					}
					$(selector).closest(".form-group").prepend(ul)
				}
			},
			success: function(response){
				var message = alertBootstrap(response.message,"success")
				var object = JSON.parse(response.object)[0]
				var fields = object.fields
				currentForm.prepend(message)
				//currentForm.trigger("reset")
				if(window.opener){
					window.opener.$(selectorInput)
						.append($("<option>",{value:response.pk,html:fields[nField]}).attr("selected",true))
						.focus()
					window.close()
				}
			}
		});
	})
}

function alertBootstrap(message,type){
	var stringHTML = '<div class="alert alert-::type:: alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;<span></button>::message::</div>'
	stringHTML = stringHTML
		.replace('::message::',message)
		.replace('::type::',type)
	return $(stringHTML)
}

$("#id_stomin").attr("data-less-than","#id_stomax");

$("[data-less-than]").change(function(event){
	var that = $(this)
	var ref = $($(this).data("less-than"));
	if($(this).val() && ref.val()){
		ref.change(function(event){that.trigger("change")})
		if($(this).val() > ref.val()) $(this).val("");
	}
});

$("[data-link-edit]").click(function(event){if(window.opener) window.close()})

$("[data-new-window]").click(function(event){
	event.preventDefault();
	if(window.location.href == this.href) {
		return;
	}
	var h = 450,
		w = 700,
		x = screen.width/2 - 700/2,
		y = screen.height/2 - h/2;
	window.open(this.href,"", "height="+h+",width="+w+",left="+x+",top="+y );
});
var languageDataTable = {
	sProcessing: "Procesando...",
	sLengthMenu: "Mostrar _MENU_ registros",
	sZeroRecords: "No se encontraron resultados",
	sEmptyTable: "Ningún dato disponible en esta tabla",
	sInfo: "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
	sInfoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
	sInfoFiltered: "(filtrado de un total de _MAX_ registros)",
	sInfoPostFix: "",
	sSearch: "Buscar:",
	sUrl: "",
	sInfoThousands: ",",
	sLoadingRecords: "Cargando...",
	oPaginate: {
		sFirst: "Primero",
		sLast: "Ãšltimo",
		sNext: "Siguiente",
		sPrevious: "Anterior"
	},
	oAria: {
		sSortAscending: ": Activar para ordenar la columna de manera ascendente",
		sSortDescending: ": Activar para ordenar la columna de manera descendente"
	}
};
