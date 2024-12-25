from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingpage'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
