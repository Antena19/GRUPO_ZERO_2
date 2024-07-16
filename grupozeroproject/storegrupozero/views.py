from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
import random
from .forms import ContactForm, RegistroForm
from .models import Artist, Technique, Product, Cart, CartItem, MensajeContacto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# VISTA INICIO
def index(request):
    products = list(Product.objects.all())
    artists = list(Artist.objects.all())
    techniques = list(Technique.objects.all())

    featured_products = random.sample(products, min(len(products), 4))
    featured_artist = random.choice(artists) if artists else None
    featured_technique = random.choice(techniques) if techniques else None

    context = {
        'featured_products': featured_products,
        'featured_artist': featured_artist,
        'featured_technique': featured_technique,
    }
    
    return render(request, 'index.html', context)

def artistas(request):
    artists = Artist.objects.all()
    return render(request, 'artistas.html', {'artists': artists})

def tecnicas(request):
    techniques = Technique.objects.all()
    return render(request, 'tecnicas.html', {'techniques': techniques})

def productos(request):
    products = Product.objects.all()
    return render(request, 'productos.html', {'products': products})

def producto_detalle(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'producto_detalle.html', {'product': product})

#VISTA REGISTRO
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Registro exitoso. ¡Bienvenido!')
                return redirect('index')
            else:
                messages.error(request, 'Error en la autenticación después del registro.')
        else:
            messages.error(request, 'Formulario no válido. Por favor, corrige los errores.')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

#VISTA LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página principal después del login
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

# CRUD CARRITO
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None, session_key=request.session.session_key)
    if not request.session.session_key:
        request.session.create()
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user if request.user.is_authenticated else None, session_key=request.session.session_key)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    cart.items.add(cart_item)
    return redirect('view_cart')

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None, session_key=request.session.session_key)
    return render(request, 'carrito.html', {'cart': cart})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user if request.user.is_authenticated else None, session_key=request.session.session_key)
    cart_item.delete()
    return redirect('view_cart')

def update_cart_item_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user if request.user.is_authenticated else None, session_key=request.session.session_key)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

#VISTA FORMULARIO CONTACTO
def formulario_contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('exito')
        else:
            messages.error(request, 'Error al enviar el mensaje. Por favor, inténtalo de nuevo.')
            return redirect('error')
    else:
        form = ContactForm()
    return render(request, 'mycontacto/formulario_contacto.html', {'form': form})

def lista_mensajes(request):
    mensajes = MensajeContacto.objects.all()
    return render(request, 'mycontacto/lista_mensajes.html', {'mensajes': mensajes})

def exito(request):
    return render(request, 'mycontacto/exito.html')

def error(request):
    return render(request, 'mycontacto/error.html')
