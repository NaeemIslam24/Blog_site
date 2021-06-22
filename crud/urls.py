from . import views
from django.urls import path


urlpatterns = [

    path('', views.register, name= 'register'),
    path('<int:rm_number>/rm/', views.delete, name= 'delete'),

]