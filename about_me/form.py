from django import forms
from .models import AboutMeDatabase


class LoginForm(forms.ModelForm):
    class Meta:
        model = AboutMeDatabase
        fields = ('name', 'second_name', 'age')
