from django.urls import path
from storegrupozero import views
from storegrupozero.views import login_view, registro

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('tecnicas/', views.tecnicas, name='tecnicas'),
    path('productos/', views.productos, name='productos'),
    path('producto/<int:product_id>/', views.producto_detalle, name='producto_detalle'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_item_quantity/<int:item_id>/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('contacto/', views.formulario_contacto, name='contacto'),
    path('contacto/exito/', views.exito, name='exito'),
    path('contacto/error/', views.error, name='error'),
    path('contacto/mensajes/', views.lista_mensajes, name='lista_mensajes'),
]
