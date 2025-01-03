from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'profile_picture', 'bio']

class SigninForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
