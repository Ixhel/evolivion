from django.http import HttpResponse

def home(request):
    return HttpResponse("Asistente para certificación en la Norma en Igualdad Laboral y No Discriminación NMX-R-025.SCFI-2015")