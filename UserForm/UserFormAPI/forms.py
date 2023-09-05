from django import forms
from .models import UserForm

class ModelForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'