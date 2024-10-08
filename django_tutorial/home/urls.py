from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('doctor/', views.doctor, name='doctor'),
    path('contact/', views.contact, name='contact'),
    path('dept/', views.department, name='dept'),
    path('payment_status/',views.payment_status,name='payment_status')
]