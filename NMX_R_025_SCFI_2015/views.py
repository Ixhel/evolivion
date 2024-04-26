from typing import Any
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from NMX_R_025_SCFI_2015.forms import LogMessageForm
from NMX_R_025_SCFI_2015.models import LogMessage

# print(request.build_absolute_uri())
# print("Asistente para certificación en la Norma en Igualdad Laboral y No Discriminación NMX-R-025.SCFI-2015")
#    return render(request, 'NMX_R_025_SCFI_2015', 
#                  {
#                      'name': name,
#                      'date': datetime.now()
#                  })

def inicio(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.log_date = datetime.now()
            empresa.save()
            return redirect("documentos")
    else: 
        return render(request, "NMX_R_025_SCFI_2015/inicio.html", {"form": form})

class lista_empresas(ListView):
    model = LogMessage
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super(lista_empresas,self).get_context_data(**kwargs)
    
def acerca(request):
    return render(request, "NMX_R_025_SCFI_2015/acerca.html")

def contacto(request):
    return render(request, "NMX_R_025_SCFI_2015/contacto.html")
