from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('uid', 'password', 'nick', 'email')

    def clean_password(self):
        return self.initial["password"]

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('uid','nick','email')

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    uid = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',    
            }
        )
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
