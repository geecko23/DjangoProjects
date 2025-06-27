from django import forms
from .models import Student

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={'fname':'First Name','lname':'Last Name','email':'Email'
                ,'phone':'Phone'}
        
        widgets={
            'fname': forms.TextInput(attrs={'class':'form1'}),
            'lname': forms.TextInput(attrs={'class':'form1'}),
            'email': forms.EmailInput(attrs={'class':'form1'}),
            'phone': forms.NumberInput(attrs={'class':'form1'}),
            'branch': forms.Select(attrs={'class':'form1'})
        }