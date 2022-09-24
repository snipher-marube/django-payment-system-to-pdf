from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('payslip/<int:pk>/', views.payslip, name='payslip')
]
