from django.shortcuts import render,redirect





def MostrarInicio(request):
   
   return render(request,'index.html')


def MostrarDetallesPelicula(request):
   
   return render(request,'movie_details.html')