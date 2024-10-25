""" User Forms """
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    """ Custom User Creation Form """
    email = forms.EmailField()

    class Meta:
        """ Meta """
        model = User
        fields = ['email', 'username', 'password1']


class ProfilePictureUpdateForm(forms.ModelForm):
    """ Profile Picture Update Form """
    picture = forms.ImageField(
        required=True,
        label='')

    class Meta:
        """ Meta """
        model = Profile
        fields = ['picture',]
