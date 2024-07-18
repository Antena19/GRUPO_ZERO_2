from django.contrib.auth.models import User
from django.db import models
from django import forms
from .utils import encrypt_message, decrypt_message

# MODELO ARTISTAS
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='artists/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# MODELO TECNICAS
class Technique(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='techniques/', null=True, blank=True)  # Agregar campo de imagen
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

# MODELO PRODUCTOS
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField(default=1)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='products')
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# MODELO CARRITO DE COMPRAS
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    items = models.ManyToManyField('CartItem', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# MODELO PARA INFORMACION CONTACTOS
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    mensaje_cifrado = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Cifra el mensaje antes de guardarlo
        self.mensaje_cifrado = encrypt_message(self.mensaje)
        super().save(*args, **kwargs)

    def get_mensaje(self):
        # Si no hay mensaje cifrado, devolver el mensaje sin cifrar
        if not self.mensaje_cifrado:
            return self.mensaje
        # Descifra el mensaje al recuperarlo
        return decrypt_message(self.mensaje_cifrado)

    def __str__(self):
        return self.nombre
