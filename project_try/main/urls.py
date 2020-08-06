
from django.contrib import admin
from django.urls import path, include
from . views import AgregateList

urlpatterns = [
    path('get-agr/<str:id_a>/<str:ds_de>/', AgregateList.as_view())
]