import re #regular expresions
from django.utils.timezone import datetime
from django.http import HttpResponse

def format_name (request, name):
    now = datetime.now()
    formatted_now = now.strftime("%d %B, %Y a las %X")
    formatted_name = re.match("[a-zA-Z]+", name)
    
    if formatted_name:
        clean_name = formatted_name.group(0)
    else:
        clean_name = "usr"
    
    content = "Usuario: " + clean_name + "Sesión iniciada: " + formatted_now
    
    return HttpResponse(content)

