var date_appen = new Date($("[name=date_appen").val())
function  calcularDigitoVerificacion ( myNit )  {
	var vpri,
		x,
		y,
		z;

	// Se limpia el Nit
	myNit = myNit.replace ( /\s/g, "" ) ; // Espacios
	myNit = myNit.replace ( /,/g,  "" ) ; // Comas
	myNit = myNit.replace ( /\./g, "" ) ; // Puntos
	myNit = myNit.replace ( /-/g,  "" ) ; // Guiones

	// Se valida el nit
	if ( isNaN ( myNit ) )  {
		console.log ("El nit/cédula '" + myNit + "' no es válido(a).") ;
		return "" ;
	};
	// Procedimiento
	vpri = new Array(16) ; 
	z = myNit.length ;

	vpri[1]  =  3 ;
	vpri[2]  =  7 ;
	vpri[3]  = 13 ; 
	vpri[4]  = 17 ;
	vpri[5]  = 19 ;
	vpri[6]  = 23 ;
	vpri[7]  = 29 ;
	vpri[8]  = 37 ;
	vpri[9]  = 41 ;
	vpri[10] = 43 ;
	vpri[11] = 47 ;  
	vpri[12] = 53 ;  
	vpri[13] = 59 ; 
	vpri[14] = 67 ; 
	vpri[15] = 71 ;

	x = 0 ;
	y = 0 ;
	for  ( var i = 0; i < z; i++ )  { 
		y = ( myNit.substr (i, 1 ) ) ;
		// console.log ( y + "x" + vpri[z-i] + ":" ) ;

		x += ( y * vpri [z-i] ) ;
		// console.log ( x ) ;    
	}

	y = x % 11 ;
	// console.log ( y ) ;

	return ( y > 1 ) ? 11 - y : y ;
}

function windowSearch(selectorInput){
	if(window.opener){
		$("[data-object-search]").click(function(){
			var value = $(this).data("object-search")
			window.opener.$(selectorInput)
				.val(value)
				.focus()
				.trigger("change")
			window.close()
		})
	}
}

function AJAXGenericView(selectorForm,selectorInput,nField,url){
	$(selectorForm).submit(function(event){
		var currentForm = $(this)
		event.preventDefault()

		var formData = new FormData(this);
		$('input[type=file]').each(function(i, file) {
			$.each(file.files, function(n, file) {
				formData.append('file-'+i, file);
			})
		})

		$.ajax({
			url: url,
			type: 'POST',
			//data: $("form").serialize(),
			data:formData,
			cache:false,
			contentType: false,
			processData: false,
			//contentType: "application/x-www-form-urlencoded",
			//contentType: 'multipart/form-data',
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

function customValidationInput(selector){
	$(selector).attr("novalidate","")

	var inputs = $(selector).find("input:invalid,select:invalid")
	console.info(inputs)
	if(inputs.length != 0){
		var element = inputs.first();
		var oHTML = element[0];
		var container = element.parent();

		console.log(element)

		element.closest(".tab-pane").addClass("active");
		element.focus();
		container.attr("title",oHTML.validationMessage);
		container.tooltip({trigger:"focus",placement:"bottom",html:true});
		container.tooltip("show");
		window.setTimeout(function(){
			container.tooltip("destroy");
		},3000);
		return {valid: false}
	}
	return {valid: true}
}

function customValidationFormTabs(selectorForm){
	$(selectorForm).attr("novalidate","")
	$(selectorForm).submit(function(){
		if($("input:invalid, select:invalid").length != 0){
			event.preventDefault();
			$(".tab-pane").removeClass("active");
			var element = $("input:invalid, select:invalid").first();
			var oHTML = element[0];
			var container = element.closest(".form-group");

			console.log(element)

			element.closest(".tab-pane").addClass("active");
			element.focus();
			container.attr("title","<span class='html_tooltip'>" + oHTML.validationMessage + "</span>");
			container.tooltip({trigger:"focus",placement:"bottom",html:true});
			container.tooltip("show");
			window.setTimeout(function(){
				container.tooltip("destroy");
			},3000);
		}
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
	if(!isNaN(parseFloat($(this).val())) && !isNaN(parseFloat(ref.val()))){
		ref.change(function(event){that.trigger("change")})
		if(parseFloat($(this).val()) > parseFloat(ref.val())) $(this).val("");
	}else{
		console.log("No se puede")
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

if($("form").length){
	$(window).on('beforeunload', function(){
		console.log("hola")
		//return "Si abandona este sitio no se guardaran los cambios que ha realizado.";

		//Esta seguro de abandonar el sitio? SI o NO
	});
}
