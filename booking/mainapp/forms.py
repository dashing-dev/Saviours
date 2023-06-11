from django import forms
from .models import Input

# creating a form
class InputForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Input
 
        # specify fields to be used
        fields = "__all__"
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'datetime_field': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }