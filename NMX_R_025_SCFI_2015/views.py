# print("Asistente para certificación en la Norma en Igualdad Laboral y No Discriminación NMX-R-025.SCFI-2015")
from typing import Any
from django import forms
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from NMX_R_025_SCFI_2015.forms import LogMessage
from NMX_R_025_SCFI_2015.forms import LogMessageForm
from NMX_R_025_SCFI_2015.forms import LogEval
from NMX_R_025_SCFI_2015.forms import LogEvalForm

#    return render(request, 'NMX_R_025_SCFI_2015', 
#                  {
#                      'name': name,
#                      'date': datetime.now()
#                  })

def inicio(request):
    form = LogMessage(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.log_date = datetime.now()
            empresa.save()
            return redirect("documentos")
    else: 
        return render(request, "NMX_R_025_SCFI_2015/inicio.html", {"form": form})

class lista_empresas(ListView):
    model = LogMessageForm
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super(lista_empresas, self).get_context_data(**kwargs)
    
class lista_resultados(ListView):
    model = LogEval
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super(lista_resultados, self).get_context_data(**kwargs)    
    
def acerca(request):
    return render(request, "NMX_R_025_SCFI_2015/acerca.html")

def contacto(request):
    return render(request, "NMX_R_025_SCFI_2015/contacto.html")
