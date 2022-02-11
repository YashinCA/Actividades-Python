from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('app.urls')),
    path('bienvenido/', include('presentacion.urls')),
    path('admin/', admin.site.urls),
]
