from django import forms
from django.forms import ModelForm
from devduck.apps.core.models import RequestPermission

class RequestForm(ModelForm):

    class Meta:
        model = RequestPermission
        fields = ['description']

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'description-request',
            'placeholder': 'Escreva o motivo da sua solicitação aqui...',
        })
    )