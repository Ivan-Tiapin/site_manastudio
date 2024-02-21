from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AssetsDB

class RegistrationFrom(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class AssetsDBForm(forms.ModelForm):
    class Meta:
        model = AssetsDB
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'style': 'height: 200px;'}),
        }