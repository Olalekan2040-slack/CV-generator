from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingpage'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('cv/preview/', views.preview_cv, name='preview_cv'),
    path('cv/download/', views.download_cv, name='download_cv'),
]
