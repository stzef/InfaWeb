import os
from django import template

from django.template import Context, Template

register = template.Library()

@register.simple_tag
#def date_appen(format_string):
def date_appen():
	return os.environ["date_appen"]
	#return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def boton_nuevo(btn_n=True,btn_s=True,btn_l=True):
	stringHTML = """<div class="text-center">
						<div class="btn-group">
							{{}}
						</div>
					</div>"""

	buttons = ""

	if btn_n:
		stringHTML_btn_n = """<button class="btn btn-app btn-info" type="reset">
								<i class="fa fa-plus-square-o"></i>Nuevo
							</button>"""
		t_stringHTML_btn_n = Template(stringHTML_btn_n)
		html_btn_n = t_stringHTML_btn_n.render(Context({}))

		buttons += str(html_btn_n)

	if btn_s:
		stringHTML_btn_s = """<button class="btn btn-app" type="submit">
								<i class="fa fa-plus-square-o"></i>Guardar
							</button>"""
		t_stringHTML_btn_s = Template(stringHTML_btn_s)
		html_btn_s = t_stringHTML_btn_s.render(Context({}))

		buttons += str(html_btn_s)

	if btn_l:
		stringHTML_btn_l = """<a data-new-window class="btn btn-app" href=""><i class="fa fa-list"></i>Listar</a>"""
		t_stringHTML_btn_l = Template(stringHTML_btn_l)
		html_btn_l = t_stringHTML_btn_l.render(Context({}))

		buttons += str(html_btn_l)

	print type(buttons)

	stringHTML = """<div class="text-center">
						<div class="btn-group">
							<button class="btn btn-app btn-info" type="reset">
								<i class="fa fa-plus-square-o"></i>Nuevo
							</button>
							<button class="btn btn-app" type="submit">
								<i class="fa fa-plus-square-o"></i>Guardar
							</button>
							<a data-new-window class="btn btn-app" href="{{href}}"><i class="fa fa-list"></i>Listar</a>
						</div>
					</div>"""

	t = Template(stringHTML)

	c = Context({'href': '#'})
	html = t.render(c)
	return html

@register.assignment_tag
def define(val = None):
	return val

@register.filter
def multiply(val_1, val_2):
	return "{:.2f}".format(val_1 * val_2)

@register.filter
def subtotal_group_invini(group):
	return "{:.2f}".format(sum((data.vunita * data.canti) for data in group))
