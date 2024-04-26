from django.urls import path

from fridayapp.views import homepage



urlpatterns = [
    path('', homepage,name='home'),
    
]
