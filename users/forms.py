from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email','username','password1']

class ProfilePictureUpdateForm(forms.ModelForm):
    picture = forms.ImageField(
        required=True,
        label='')
    class Meta:
        model = Profile
        fields = ['picture',]