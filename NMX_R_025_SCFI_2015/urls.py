from django.urls import path
from NMX_R_025_SCFI_2015 import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("docs/", views.documentos, name="documentos"),
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto"),
    #path("NMX_R_025_SCFI_2015/<name>", format.format_name, name="format_name" )
]
