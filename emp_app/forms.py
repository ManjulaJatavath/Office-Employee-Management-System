# forms.py
from django import forms
from .models import Department, Employee, Role

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'salary', 'bonus', 'phone', 'dept', 'role']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['dept'].queryset = Department.objects.all()
        self.fields['role'].queryset = Role.objects.all()