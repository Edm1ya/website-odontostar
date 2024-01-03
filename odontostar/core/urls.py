from django.urls import path
from .views import HomePageView, FormDateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form-date/', FormDateView.as_view(), name='form-date'),
]
