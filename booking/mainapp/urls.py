from django.contrib import admin
from django.urls import path , include 
from . import views 

urlpatterns = [
    path('', views.index , name='index'),
    path('personal/', views.create_view , name='create_view'),
    # path('list', views.list_view , name ='list_view '),
    path('<id>/update', views.update_view , name='update_view'),
    path('<id>/delete', views.delete_view , name='delete_view'),
    path('adminpage', views.adminpage , name='adminpage'),
    path('social/', views.social , name='social'),
    path('helpline/', views.helpline , name='helpline'),
    
]