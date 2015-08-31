from django import forms
from registration.forms import RegistrationFormUniqueEmail

class UsuarioFriendsForm(RegistrationFormUniqueEmail):
	nickname = forms.CharField()
