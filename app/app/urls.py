

from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from core.views import  home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('home/',home_view ),
]
