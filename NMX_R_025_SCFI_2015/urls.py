from django.urls import path
from NMX_R_025_SCFI_2015 import views
from NMX_R_025_SCFI_2015.models import LogMessage

# Hacer variables por cada nueva vista de lista

vista_empresa = views.lista_empresas.as_view(
    queryset = LogMessage.objects.order_by("-log_date")[:],
    context_object_name = "corp_list",
    template_name = "NMX_R_025_SCFI_2015/documentos.html",
)

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("docs/", vista_empresa, name="documentos"),
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto"),
    #path("NMX_R_025_SCFI_2015/<name>", format.format_name, name="format_name" )
]
