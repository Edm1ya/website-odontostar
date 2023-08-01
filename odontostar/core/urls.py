from django.urls import path
from .views import HomePageView, ContactPageView, FormDateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('form-date/', FormDateView.as_view(), name='form-date'),
]
