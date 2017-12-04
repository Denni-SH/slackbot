from django import forms
from .models import CustUser, Team
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('channel_id',)
