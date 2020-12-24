from django.urls import path

from . import views

urlpatterns = [
    path('generate-idea', views.generateIdea)
]

