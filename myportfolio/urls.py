from django.urls import path
from . import views


app_name='myportfolio'
urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
]
