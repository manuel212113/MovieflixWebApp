from django.contrib import admin
from .views import MostrarInicio,MostrarDetallesPelicula
from django.urls import path,include

urlpatterns = [
    path('home/', MostrarInicio, name="inicio" ),
    path('home/details/', MostrarDetallesPelicula, name="detalles_peli" ),
    path('admin/', admin.site.urls),
]