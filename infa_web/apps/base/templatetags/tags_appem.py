from infa_web.parameters import ManageParameters

register = template.Library()

@register.simple_tag
def get_name_theme_app(request_db):
	manageParameters = ManageParameters(request_db)
	theme_app = manageParameters.get_param_value('theme_presentation')
	return theme_app
