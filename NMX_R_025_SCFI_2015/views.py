from django.http import HttpResponse
from django.shortcuts import render

## print(request.build_absolute_uri())
#    print("Asistente para certificación en la Norma en Igualdad Laboral y No Discriminación NMX-R-025.SCFI-2015")
#    return render(request, 'NMX_R_025_SCFI_2015', 
#                  {
#                      'name': name,
#                      'date': datetime.now()
#                  })



def inicio(request):
    return render(request, "NMX_R_025_SCFI_2015/inicio.html")

def acerca(request):
    return render(request, "NMX_R_025_SCFI_2015/acerca.html")

def contacto(request):
    return render(request, "NMX_R_025_SCFI_2015/contacto.html")