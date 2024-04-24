from django.http import HttpResponse
from django.shortcuts import render

def home(request, name):
    print(request.build_absolute_uri())
    print("Asistente para certificación en la Norma en Igualdad Laboral y No Discriminación NMX-R-025.SCFI-2015")
    return render(request, 'NMX_R_025_SCFI_2015', 
                  {
                      'name': name,
                      'date': datetime.now()
                  })
