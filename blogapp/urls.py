from . import views
from django.urls import path

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name= 'post'),
    path('<int:number>/<slug:title>/', views.single_post, name= 'single_post'),


]