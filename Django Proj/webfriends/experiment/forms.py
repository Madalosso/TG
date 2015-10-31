from django import forms
from registration.forms import RegistrationFormUniqueEmail
from .models import Algorithms, ExecModel


class UsuarioFriendsForm(RegistrationFormUniqueEmail):
    nickname = forms.CharField(required=False)
    company = forms.CharField(required=False)


class ExecutionForm(forms.Form):
    PresetExecution = forms.ModelChoiceField(queryset=ExecModel.objects.all(),
                                             empty_label="---Selecione um modelo---",
                                             required=False)
    Algorithm = forms.ModelChoiceField(queryset=Algorithms.objects.all(),
                                       empty_label="---Selecione um algoritmo---",
                                       required=True,
                                       to_field_name="nameAlg",
                                       )
    opt = forms.CharField(required=False)
    FileIn = forms.FileField(required=False)


class ContactForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()
