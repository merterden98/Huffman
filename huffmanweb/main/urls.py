from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home.as_view(), name='home'),
    path('home/demo/', views.demo.as_view(), name='demo'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]