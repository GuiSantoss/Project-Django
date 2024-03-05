from django import forms
from utils.django_forms import add_palceholder

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_palceholder(self.fields['username'], 'Type your username')
        add_palceholder(self.fields['password'], 'Type your password')


    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )