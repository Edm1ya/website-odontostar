from django.shortcuts import render
from django.views.generic.base import TemplateView
from services.models import Service
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context

class ContactPageView(TemplateView):
    template_name = 'core/contact.html'

class FormDateView(TemplateView):
    template_name = 'core/form-date.html'