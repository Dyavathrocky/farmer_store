from django.urls import path
from .views import Home , AboutPage

urlpatterns = [
    path('about/', AboutPage.as_view(), name='about'),
    path('',Home.as_view(),name='home'),  
]
