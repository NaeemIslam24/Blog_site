from . import views
from django.urls import path

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name= 'post'),
    path('<int:number>/<slug:title>/', views.single_post, name= 'single_post'),
    path('tag/<slug:tag_slug>',views.index, name='post_list_by_tag'),
    path('<int:post_id>/share/',views.post_share, name='post_share'),


]