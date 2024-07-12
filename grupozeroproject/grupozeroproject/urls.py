# grupozeroproject/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storegrupozero.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluir URLs de autenticación de Django
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


