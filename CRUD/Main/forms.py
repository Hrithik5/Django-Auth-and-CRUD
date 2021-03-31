from django import forms
from .models import  Information

class InfoCreate(forms.ModelForm):

    class Meta:
        model = Information
        fields = '__all__'