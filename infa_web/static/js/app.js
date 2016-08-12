$("[data-new-window]").click(function(event){
	event.preventDefault()
	var h = 450,
		w = 700,
		x = screen.width/2 - 700/2,
		y = screen.height/2 - h/2;
		
	window.open(this.href,"", "height="+h+",width="+w+",left="+x+",top="+y )
})
