# storegrupozero/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm  # Importa tu formulario de contacto
from .models import Artist, Technique, Product, Cart, CartItem  # Importa tus modelos
from django.urls import reverse_lazy

def index(request):
    # Obtener los últimos 4 artistas, técnicas y productos para mostrar en el index
    latest_artists = Artist.objects.order_by('-created_at')[:4]
    latest_techniques = Technique.objects.order_by('-created_at')[:4]
    latest_products = Product.objects.order_by('-created_at')[:4]
    
    context = {
        'latest_artists': latest_artists,
        'latest_techniques': latest_techniques,
        'latest_products': latest_products,
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

def login_view(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            
            # Aquí puedes agregar la lógica para enviar el correo electrónico
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}',
                'tu_email@tudominio.com',  # Cambia esto por tu dirección de correo electrónico
                ['destinatario@dominio.com'],  # Cambia esto por la dirección de correo del destinatario
                fail_silently=False,
            )
            
            return render(request, 'contacto_exito.html')  # Página de éxito
    else:
        form = ContactForm()

    return render(request, 'formulario_contacto.html', {'form': form})

def ver_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'ver_contactos.html', {'contactos': contactos})
