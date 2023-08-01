from django.urls import path
from .views import ServicesListView, ServiceDetailView

urlpatterns = [
    path('',ServicesListView.as_view(), name='services'),
    path('service/<int:pk>/',ServiceDetailView.as_view(), name='service'),
]
