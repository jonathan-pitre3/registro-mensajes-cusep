from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.services, name='servicios'),
    path('sobre-nosotros/', views.about, name='sobre_nosotros'),
    path('solicitar/', views.intake_form, name='solicitar'),
    path('solicitud-enviada/', views.submitted, name='solicitud_enviada'),
]
