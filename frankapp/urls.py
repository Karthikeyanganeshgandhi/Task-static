from django.urls import path
from . import views

urlpatterns = [
    path('gkpage/',views.gkpage,name='gkpage'),
]