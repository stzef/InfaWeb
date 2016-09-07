import os
from django import template

register = template.Library()

@register.simple_tag
#def date_appen(format_string):
def date_appen():
	return os.environ["date_appen"]
	#return datetime.datetime.now().strftime(format_string)

@register.assignment_tag
def define(val = None):
	return val

@register.filter
def multiply(val_1, val_2):
	return "{:.2f}".format(val_1 * val_2)

@register.filter
def subtotal_group_invini(group):
	return "{:.2f}".format(sum((data.vunita * data.canti) for data in group))