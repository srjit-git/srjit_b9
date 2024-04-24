from django import forms
from student.models import Department



class Dept_form(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

