from django import forms
from .models import AboutMeDatabase


class LoginForm(forms.ModelForm):
    """
    Login form.
    """
    class Meta:
        """
        Data for login.
        """
        model = AboutMeDatabase
        fields = ('name', 'second_name', 'age')
