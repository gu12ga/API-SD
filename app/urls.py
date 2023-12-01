from django.urls import path
from . import views

urlpatterns = [
    path('leitor/', views.leitor, name='leitor'),
    path('ilumina/', views.ilumina, name='ilumina'),
]
