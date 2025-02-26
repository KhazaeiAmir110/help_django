from django import forms

from users.models import User


class RegistrationForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
