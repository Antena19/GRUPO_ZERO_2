# storegrupozero/urls.py
from django.urls import path, include
from storegrupozero import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('tecnicas/', views.tecnicas, name='tecnicas'),
    path('productos/', views.productos, name='productos'),
    path('producto/<int:product_id>/', views.producto_detalle, name='producto_detalle'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', views.contact, name='contacto'),  # URL para el formulario de contacto
    path('ver_contactos/', views.ver_contactos, name='ver_contactos'),  # URL para ver los registros de contactos
]