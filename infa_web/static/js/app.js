var date_appen = new Date($("[name=date_appen").val())
format_date_appen = "YYYY-MM-DD"

jQuery.fn.extend({
	inputCurrency : function(){
		var input = this,
			regexp = /^\$ (?!0\.00)[1-9]\d{0,2}(,\d{3})*(\.\d\d)?$/
		input.css({"text-align":"right"})

		//Selecciona todo lo que no sea un nuemro, una coma, un punto o un espacio
		var regexp_clear = /([^0-9|\$|\,|\.|\s])/g

		input.change(function(){
			input = $(this)
			input.val(input.val().replace(regexp_clear,""))
			if (!regexp.test(input.val())){
				var valueInput = input.val(),
					clearValue = valueInput.replace(/ /g,"").replace(/,/g,"").replace(/\./g,"").replace(/\$/g,"").trim()

				input.val(currencyFormat.format(clearValue))
			}
		})

		if(input.val() == "") {
			input.val( "$ 0")
		}else{
			input.trigger("change")
		}

	},
	custom_format_val : function(){
		var val = ""
		if (this.hasClass("input-currency")){
			val = currencyFormat.sToN(this.val()).toString()
		}else{
			val = this.val()
		}
		return val
	}
})

$('[check-carlos]').change(function(){
	var input_value = this.value
	var fn = eval($(this).data("fn"))
	if(!input_value){
		if(fn) fn(null)
		return
	}
	$.post('/api/get-object/',JSON.stringify({'model': 5,'field': this.name,'value': input_value}),function(response){
		if(response.object){
			var object = JSON.parse(response.object)[0]
			fields = object.fields
			if(fn) fn(fields)
			return
		}else{
			$.post('/api/get-object/',JSON.stringify({'model': 5,'field': "cbarras",'value': input_value}),function(response){
				if(response.object){
					var object = JSON.parse(response.object)[0]
					fields = object.fields
				}else{
					$('#id_carlos').val("")
					tooltipBootstrap($('#id_carlos'),".input-group","Este Articulo no se encuentra registrado.")
				}
				if(fn) fn(fields)
			})
		}
	})
});


$("input").focus(function(){$(this).select()})
$(document).on("click", ".open-modal", function(e){
	$('#Modal').load($(this).attr('href'),function(){
		$('#Modal').modal({
			show:true
		});
	});
	return false;
});
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

function defaultfn(){}


$("button[action=reset-form]").click(function (e){
	console.log("Action Reset Form")
	$(this).closest("form")
		.trigger("reset")
		.find(":input")
		.trigger("change")
})

function AJAXGenericView(selectorForm,selectorInput,nField,url,callback,messageWait){
	$(selectorForm).submit(function(event){
		var currentForm = $(this)
		event.preventDefault()

		console.log(this)

		var formData = new FormData(this);
		$('input[type=file]').each(function(i, file) {
			$.each(file.files, function(n, file) {
				formData.append('file-'+i, file);
			})
		})

		$(this).find(".input-currency").toArray().forEach(function(ic){
			nVal = currencyFormat.sToN($(ic).val())
			formData.set(ic.name,nVal)
		})

		loading_animation(messageWait)

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
				$(".animation").empty()
				if (typeof callback == "function") callback(null,response)
				$('<ul class="errorlist"></ul>')
				var data = JSON.parse(response.responseText)
				for (field in data.errors){
					var ul = $('<ul class="errorlist"></ul>')
					var selector = "[name=" + field + "]"
					for (var error of data.errors[field]){
						var message = alertBootstrap(error,"danger")
						ul.append($("<li>").append(message))
					}
					$(selector).closest(".form-group").find("ul.errorlist").remove()
					$(selector).closest(".form-group").prepend(ul)
				}
			},
			success: function(response){
				$(".animation").empty()
				var message = alertBootstrap(response.message,"success")
				var object = JSON.parse(response.object)[0]
				var fields = object.fields
				currentForm.prepend(message)
				//currentForm.trigger("reset")
				if (typeof callback == "function") callback(response,null)
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

function customValidationFormTabs(selectorForm,fn){
	$(selectorForm).attr("novalidate","")
	$(selectorForm).submit(function(){
		if($("input:invalid, select:invalid").length != 0){
			event.preventDefault();
			$(".tab-pane").removeClass("active");
			var element = $("input:invalid, select:invalid").first();
			var oHTML = element[0];
			var container = element.closest(".form-group");

			console.log(element)

			var tab = element.closest(".tab-pane").addClass("active");

			console.info(tab)

			$(".nav.nav-pills li").removeClass("active");
			$("[href='#" + tab.attr("id") + "']").closest("li").addClass("active");

			element.focus();
			container.attr("title","<span class='html_tooltip'>" + oHTML.validationMessage + "</span>");
			container.tooltip({trigger:"focus",placement:"bottom",html:true});
			container.tooltip("show");
			window.setTimeout(function(){
				container.tooltip("destroy");
			},3000);

			fn(false)
			return false
		}
		fn(true)
		return false
	})
}

function tooltipBootstrap(element,selectorParent,message,time){
	time = time || 3000
	var container = element.closest(selectorParent);

	container.attr("title","<span class='html_tooltip'>" + message + "</span>");
	container.tooltip({trigger:"focus",placement:"bottom",html:true});
	container.tooltip("show");
	window.setTimeout(function(){
		container.tooltip("destroy");
	},time);
}

document.body.addEventListener("DOMNodeInserted", function (ev) {
	//console.log("DOMNodeInserted")
	ev.target
	if($(ev.target).hasClass("alert","alert-dismissible")){
		$(ev.target)[0].scrollIntoView()
		window.setTimeout(function(){
			$(ev.target).remove()
		},6000)
	}
	//$("[data-new-window]").off("click",open_new_window)
	$("[data-new-window]").off("click")
	$("[data-new-window]").click(open_new_window);
}, false);

function open_new_window(event){
	event.preventDefault();
	if(window.location.href == this.href) {
		return;
	}
	var h = 650,
		w = 1000,
		x = screen.width/2 - w/2,
		y = screen.height/2 - h/2;
	window.open(this.href,"", "height="+h+",width="+w+",left="+x+",top="+y);
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
	var h = 650,
		w = 1000,
		x = screen.width/2 - w/2,
		y = screen.height/2 - h/2;
	window.open(this.href,"", "height="+h+",width="+w+",left="+x+",top="+y);
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

function CurrencyFormat(){
	//numberFormat = Intl.NumberFormat({style:"currency",currency:"COP",currencyDisplay:"symbol"})
	this.numberFormat = Intl.NumberFormat("es-419")
}

CurrencyFormat.prototype.format = function(number){
	if(this.numberFormat.format(number) == "NaN") return "$ 0"
	return "$ " + this.numberFormat.format(number)
}
CurrencyFormat.prototype.clear = function(number){
	return number.replace(",","").replace("$","").trim()
}
CurrencyFormat.prototype.sToN = function(s){
	var n = parseFloat(s.replace(/ /g,"").replace(/,/g,"").replace(/\./g,"").replace(/\$/g,"").trim())
	return n
}

var currencyFormat = new CurrencyFormat()

$("[data-currency-format]").change(function(event){
	var currencyFormat = CurrencyFormat()
	$(this).val(currencyFormat.format($(this).val()))
})

$(document).on("click", "#next", function(){
	if(!$(".next").hasClass('disabled')){
		$(".previous").removeClass('disabled')
		cont += 1
		data_table()
	}
})
$(document).on("click", "#previous", function(){
	if(!$(".previous").hasClass('disabled')){
		if(cont == 2){
			$(".previous").addClass('disabled')
		}
		cont -= 1
		data_table()
	}
})
$(document).on("change", ".orderBy", function(){
	data_table()
});
$(document).on("change", ".buscarPor", function(){
	data_table()
})
$(document).on("change", ".orderTipo", function(){
	data_table()
})
$(window).on('beforeunload', function (e) {
	localStorage.clear();
});

//$(document).ready(function(e){
	if(window.opener){
		console.warn("Hola")

		var button = $("<button type='button' class='btn btn-app' ><i class='fa fa-close'></i>Salir</button>")
			.click(function(){
				window.close()
			})

		if($(".btn-group").length == 1){
			$(".btn-group").append(button)
		}else{
			$(".content-wrapper").append(button)
		}
	}
//})

$(document).ready(function(e){
	$(".input-currency").inputCurrency()
})
