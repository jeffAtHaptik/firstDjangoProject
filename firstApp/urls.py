from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employee_id>/', views.detail, name='detail'),
    path('<int:company_id>/employees/', views.companywiseemplyee, name='companywiseemplyee')
]