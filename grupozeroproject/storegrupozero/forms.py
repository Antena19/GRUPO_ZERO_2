# storegrupozero/forms.py
from django import forms
from .models import MensajeContacto
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

#FORMULARIO CONTACTO
class ContactForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'correo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu mensaje', 'rows': 3}),
        }

#FORMULARIO REGISTRO
class RegistroForm(forms.ModelForm):
    email = forms.EmailField(label='Correo', error_messages={
        'required': 'Este campo es obligatorio.',
        'invalid': 'Introduce una dirección de correo electrónico válida.',
    })
    username = forms.CharField(label='Nombre de usuario', max_length=150, error_messages={
        'required': 'Este campo es obligatorio.',
        'max_length': 'El nombre de usuario no puede tener más de 150 caracteres.',
    })
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='La contraseña debe tener al menos 8 caracteres.', error_messages={
        'required': 'Este campo es obligatorio.',
    })

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está en uso.')
        return email