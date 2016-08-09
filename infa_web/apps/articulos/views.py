from django.shortcuts import render
from django.views.generic import CreateView

from infa_web.apps.articulos.models import *
from infa_web.apps.articulos.forms import *

class ArticleCreate(CreateView):
	model = Arlo
	template_name = "articulos/add-article.html"
	form = addArticle
	fields = ["carlos","cbarras","cgpo","ncorto","nlargo","canti","vcosto","ifcostear","ifpvfijo","cesdo","ciudad","ivas_civa","stomin","stomax","pvta1","pvta2","pvta3","pvta4","pvta5","pvta6","citerce1","vcosto1","fcosto1","citerce2","vcosto2","fcosto2","citerce3","vcosto3","fcosto3","ifedinom","refe","cmarca","ifdesglo","mesesgara","cubica","porult1","porult2","porult3","porult4","porult5","porult6","foto1","foto2","foto3",]
