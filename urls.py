from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.Charge, name='charge'),
    path('', views.HomePageView.as_view(), name='home'),
]
