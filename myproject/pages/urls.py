from django.urls import path
from .views import save_employee,home

urlpatterns = [
    path('save-employee/', save_employee, name='save_employee'),
    path('', home, name='home'),
    # Add other URL patterns as needed
]
#from . import views

#urlpatterns = [
#    path('', views.home, name='home'),
#]