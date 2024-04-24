from django.urls import path
from NMX_R_025_SCFI_2015 import views

urlpatterns = [
    path("", views.home, name="inicio"),
    #path("NMX_R_025_SCFI_2015/<name>", format.format_name, name="format_name" )
]
