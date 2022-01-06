from django import forms
from .models import Department


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'