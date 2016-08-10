from django import forms

class InventoryForm(forms.Form):
	codigo = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'required': True}))