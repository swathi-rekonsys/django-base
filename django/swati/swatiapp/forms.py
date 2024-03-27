from django import forms
from swatiapp.models import SwathiDetails

class SwathiForm(forms.ModelForm):
    class Meta:
        model=SwathiDetails
        fields='__all__'