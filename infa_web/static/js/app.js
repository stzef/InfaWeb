if(window.opener){
	console.log(window.opener)
}
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
