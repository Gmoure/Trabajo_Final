from django.shortcuts import render
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from vuelos.models import Vuelos
from vuelos.forms import VueloForm, Buscar
from django.views import View

def mostrar_vuelos(request):
  lista_vuelos = Vuelos.objects.all()
  return render(request, "vuelos/vuelos.html", {"lista_vuelos": lista_vuelos})

class BuscarVuelo(View):

    form_class = Buscar
    template_name = 'vuelos/buscar_vuelo.html'
    initial = {"destino":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            destino = form.cleaned_data.get("destino")
            lista_vuelos = Vuelos.objects.filter(destino__icontains=destino).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vuelos':lista_vuelos})
        return render(request, self.template_name, {"form": form})


class AltaVuelo(View):
    
    form_class = VueloForm
    template_name = 'vuelos/alta_vuelo.html'
    initial = {"destino":"", "fecha_vuelo_ida":"" , "fecha_vuelo_vuelta": ""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se ha reservado su vuelo a {form.cleaned_data.get('destino')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                            'msg_exito': msg_exito})
            
        return render(request, self.template_name, {"form": form})