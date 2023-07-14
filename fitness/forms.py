from typing import Any
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','fullname','username','password1','password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['fullname'].required = False
        self.fields['username'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False

        
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            # Verifico que el email no exista previamente
            cuenta = CustomUser.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError('La dirección de correo ya se está utilizando')
    
    def clean_fullname(self):
        fullname = self.cleaned_data['fullname'].lower().title()
        
        # last_name = self.cleaned_data['last_name'].lower().title()
        # fullname = f"{first_name} {last_name}"
        return fullname
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            # Verifico que el username no exista previamente
            cuenta = CustomUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'El nombre de usuario {username} ya se está utilizando')
    
    def compare_passwords(self):
        pw1 = self.cleaned_data['password1']
        pw2 = self.cleaned_data['password2']
        if pw1 != pw2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        else:
            return pw1