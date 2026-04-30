from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cusep-admin/', admin.site.urls),
    path('', include('public_site.urls')),
]
