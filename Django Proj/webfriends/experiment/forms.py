from django import forms
from registration.forms import RegistrationFormUniqueEmail

class UsuarioFriendsForm(RegistrationFormUniqueEmail):
	nickname = forms.CharField()

class ExecutionForm(forms.Form):
	status = forms.IntegerField()

class ContactForm(forms.Form):
	nome = forms.CharField()
	email = forms.EmailField()
	mensagem = forms.CharField()
	arquivo = forms.FileField(required=False)