from infa_web.apps.terceros.models import *

tercero = Tercero.objects.get(pk=1)


data_mvens = [
	{
		"base":{
			"mode_view":"create",
			"cmven":"",
			"ctimo":"1001",
			"fmven":"2016-10-13",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"RA00001",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":True,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 20,
				"vunita" : 800
			}
		]
	},
	{
		"base":{
			"mode_view":"create",
			"cmven":"",
			"ctimo":"1001",
			"fmven":"2016-10-15",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"RA00002",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":True,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 10,
				"vunita" : 1000
			}
		]
	},
	{
		"base":{
			"mode_view":"create",
			"cmven":"",
			"ctimo":"1001",
			"fmven":"2016-10-16",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"RA00003",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":True,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 10,
				"vunita" : 3000
			}
		]
	},
	{
		"base":{
			"mode_view":"create",
			"cmven":"",
			"ctimo":"1001",
			"fmven":"2016-10-17",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"RA00004",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":True,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 10,
				"vunita" : 2500
			}
		]
	},
	{
		"base":{
			"mode_view":"create",
			"cmven":"",
			"ctimo":"1001",
			"fmven":"2016-10-18",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"RA00005",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":True,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 10,
				"vunita" : 1833
			}
		]
	},
]

data_mvsas = [
	{
		"base":{
			"mode_view":"create",
			"cmvsa":"",
			"ctimo":"2001",
			"fmvsa":"2016-10-14",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"SA00001",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":False,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 15,
				"vunita" : 800
			}
		]
	},
]
"""
	{
		"base":{
			"mode_view":"create",
			"cmvsa":"",
			"ctimo":"2001",
			"fmvsa":"2016-10-19",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"docrefe":"SA00002",
			"descri":"-",
			"cesdo":"1",
			"cbode0":"1",
			"vttotal":0,
			"is_input_movement":False,
			"mvdeta":[]
		},
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 20,
				"vunita" : 2083
			},
		]
	},
"""
data_invs = [
	{
		"cii" : "",
		"deta" : [
			{
				"carlos":"1000",
				"nlargo":"Huevo A",
				"cancalcu":0,
				"canti":100,
				"vcosto":200,
				"ajuent":100,
				"ajusal":0,
				"cbarras":""
			},
			{
				"carlos":"1001",
				"nlargo":"Huevo B",
				"cancalcu":0,
				"canti":200,
				"vcosto":250,
				"ajuent":200,
				"ajusal":0,
				"cbarras":""
			}
		]
	}
]
"""
	{
		"cmpago" : 1000,
		"nmpago" : "Efectivo",
		"porcentaje" : 0,
	},
	{
		"cmpago" : 1001,
		"nmpago" : "Tarjeta",
		"porcentaje" : 0,
	},
	{
		"cmpago" : 1002,
		"nmpago" : "Cheque",
		"porcentaje" : 0,
	},
	{
		"cmpago" : 1003,
		"nmpago" : "Nota Credito",
		"porcentaje" : 0,
	},
"""
data_facs = [
	{
		"base":{ 
			"mode_view":"create",
			"cfac":"",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"cvende":"1",
			"cdomici":"1",
			"ctifopa":"1001",
			"femi":"2016-10-19",
			"fpago":"2016-10-19",
			"cemdor":"1",
			"ccaja":"1",
			"cesdo":"1",
			"descri":"",
			"vttotal":0,
			"ventre":0,
			"vcambio":0,
			"vtbase":0,
			"vtiva":0,
			"brtefte":0,
			"prtefte":0,
			"vrtefte":0,
			"vflete":0,
			"vdescu":0,
			"it":"",
			"cmpago":"",
			"vmpago":"",
			"medios_pagos":[],
			"mvdeta":[]
		},
		"medios_pagos":[
				{
					"cmpago" : 1000,
					"nmpago" : "Efectivo",
					"porcentaje" : 50,
					"docmpago" : 0,
					"banmpago" : 1000,
				},
		],
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 20,
				"vunita" : 2083,
				"pordes" : 0,
				"civa" :1,
			},
		],
	},
	{
		"base":{ 
			"mode_view":"create",
			"cfac":"",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"cvende":"1",
			"cdomici":"1",
			"ctifopa":"1001",
			"femi":"2016-10-25",
			"fpago":"2016-10-25",
			"cemdor":"1",
			"ccaja":"1",
			"cesdo":"1",
			"descri":"",
			"vttotal":0,
			"ventre":0,
			"vcambio":0,
			"vtbase":0,
			"vtiva":0,
			"brtefte":0,
			"prtefte":0,
			"vrtefte":0,
			"vflete":0,
			"vdescu":0,
			"it":"",
			"cmpago":"",
			"vmpago":"",
			"medios_pagos":[],
			"mvdeta":[]
		},
		"medios_pagos":[],
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 1,
				"vunita" : 1000,
				"pordes" : 0,
				"civa" :1,
			},
		],
	},
	{
		"base":{ 
			"mode_view":"create",
			"cfac":"",
			"citerce":tercero.pk,
			"name__citerce":tercero.rasocial,
			"cvende":"1",
			"cdomici":"1",
			"ctifopa":"1001",
			"femi":"2016-10-25",
			"fpago":"2016-10-25",
			"cemdor":"1",
			"ccaja":"1",
			"cesdo":"1",
			"descri":"",
			"vttotal":0,
			"ventre":0,
			"vcambio":0,
			"vtbase":0,
			"vtiva":0,
			"brtefte":0,
			"prtefte":0,
			"vrtefte":0,
			"vflete":0,
			"vdescu":0,
			"it":"",
			"cmpago":"",
			"vmpago":"",
			"medios_pagos":[],
			"mvdeta":[]
		},
		"medios_pagos":[
				{
					"cmpago" : 1000,
					"nmpago" : "Efectivo",
					"porcentaje" : 50,
					"docmpago" : 0,
					"banmpago" : 1000,
				},
				{
					"cmpago" : 1002,
					"nmpago" : "Cheque",
					"docmpago" : 124657987,
					"porcentaje" : 50,
					"banmpago" : 1001,
				},
		],
		"deta":[
			{
				"carlos" : 1000,
				"canti" : 40,
				"vunita" : 1500,
				"pordes" : 0,
				"civa" :1,
			},
		],
	},
]

data_edit_facs = data_facs
data_edit_facs[0]["medios_pagos"] = [
	{
		"cmpago" : 1000,
		"nmpago" : "Efectivo",
		"porcentaje" : 100,
		"docmpago" : 0,
		"banmpago" : 1000,
	},
]
data_edit_facs[2]["medios_pagos"] = [
	{
		"cmpago" : 1000,
		"nmpago" : "Efectivo",
		"porcentaje" : 100,
		"docmpago" : 0,
		"banmpago" : 1000,
	}
]

data_articles = [
	{
		"cbarras":"",
		"cgpo":1,
		"ncorto":"Huevo A",
		"nlargo":"Huevo A",
		"canti":0,
		"vcosto":0,
		"ifcostear":True,
		"ifpvfijo":False,
		"cesdo":1,
		"ctiarlo":1,
		"cunidad":1,
		"ivas_civa":1,
		"stomin":"1",
		"stomax":"100",
		"pvta1":"250",
		"pvta2":0,
		"pvta3":0,
		"pvta4":0,
		"pvta5":0,
		"pvta6":0,
		"vcosto1":0,
		"vcosto2":0,
		"vcosto3":0,
		"ifedinom":False,
		"refe":"",
		"cmarca":1,
		"ifdesglo":False,
		"mesesgara":0,
		"cubica":1,
		"porult1":0,
		"porult2":0,
		"porult3":0,
		"porult4":0,
		"porult5":0,
		"porult6":0,
		"foto1":"img/articles/default.jpg",
		"foto2":"img/articles/default.jpg",
		"foto3":"img/articles/default.jpg"
	},
	{
		"cbarras":"",
		"cgpo":1,
		"ncorto":"Huevo B",
		"nlargo":"Huevo B",
		"canti":0,
		"vcosto":0,
		"ifcostear":True,
		"ifpvfijo":False,
		"cesdo":1,
		"ctiarlo":1,
		"cunidad":1,
		"ivas_civa":1,
		"stomin":"1",
		"stomax":"100",
		"pvta1":"300",
		"pvta2":0,
		"pvta3":0,
		"pvta4":0,
		"pvta5":0,
		"pvta6":0,
		"vcosto1":0,
		"vcosto2":0,
		"vcosto3":0,
		"ifedinom":False,
		"refe":"",
		"cmarca":1,
		"ifdesglo":False,
		"mesesgara":0,
		"cubica":1,
		"porult1":0,
		"porult2":0,
		"porult3":0,
		"porult4":0,
		"porult5":0,
		"porult6":0,
		"foto1":"img/articles/default.jpg",
		"foto2":"img/articles/default.jpg",
		"foto3":"img/articles/default.jpg"
	}
]

costing_and_stock_expected_values = {
	1000:{
		"canti" : 84,
		"vcosto" : 791.93,
	},
	1001:{
		"canti" : 200,
		"vcosto" : 250,
	},
}
