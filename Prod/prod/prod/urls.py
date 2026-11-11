from django.contrib import admin
from django.urls import path
from prodapp import views

urlpatterns = [
    path('reports/', views.all_reports, name='all_reports'),
]