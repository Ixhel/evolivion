from django.urls import path
from NMX_R_025_SCFI_2015 import views

urlpatterns = [
    path("", views.home, name="inicio"),
]
