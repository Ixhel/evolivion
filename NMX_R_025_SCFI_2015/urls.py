from django.urls import path
from NMX_R_025_SCFI_2015 import views
from NMX_R_025_SCFI_2015.models import LogMessage
from NMX_R_025_SCFI_2015.models import LogEval

# Hacer variables por cada nueva vista de lista

vista_empresa = views.lista_empresas.as_view(
    queryset = LogMessage.objects.order_by("-log_date")[:],
    context_object_name = "corp_list",
    template_name = "NMX_R_025_SCFI_2015/documentos.html",
)

vista_evaluacion = views.lista_resultados.as_view(
    queryset = LogEval.objects.order_by("-id")[:], # Función que calcula puntuacion en una lista de valores. Correspondencia a rango de valores (DB)
    context_object_name = "result_list",
    template_name = "NMX_R_025_SCFI_2015/evaluacion.html",
)

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("docs/", vista_empresa, name="documentos"),
    path("evaluacion/", vista_evaluacion, name="evaluacion"),
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto"),
    #path("NMX_R_025_SCFI_2015/<name>", format.format_name, name="format_name" )
]
