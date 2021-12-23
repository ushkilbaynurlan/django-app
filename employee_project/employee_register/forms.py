from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Толық аты',
            'emp_code':'Код'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "таңдау"
        self.fields['emp_code'].required = False
