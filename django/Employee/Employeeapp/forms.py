from django import forms
from Employeeapp.models import EmployeeDetails


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeDetails
        fields='__all__'