from django import forms
from django.contrib.auth.models import User


class Login_form(forms.ModelForm):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')



class Update_profile(forms.ModelForm):

    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')