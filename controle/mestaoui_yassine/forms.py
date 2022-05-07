from django import forms
from django.shortcuts import render

from .models import Client, Compte, Operation


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class CompteForm(forms.ModelForm):
    class Meta:
        model = Compte
        fields = "__all__"

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = "__all__"