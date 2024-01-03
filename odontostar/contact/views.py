from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms  import ContactForm
from .models import Contact

# Create your views here.
class ContactPageView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')