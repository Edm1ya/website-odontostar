from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Service
# Create your views here.

class ServicesListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service