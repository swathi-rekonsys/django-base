from django import forms
from login_credentialsapp.models import SwatiDetails

class SwatiForm(forms.ModelForm):
    class Meta:
        model=SwatiDetails
        fields='__all__'