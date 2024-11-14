from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/<int:pk>/', views.group, name='group'),
    path('group/new/', views.new_group, name='new_group'),
    path('group/<int:pk>/edit/', views.edit_group, name='edit_group'),
    path('group/<int:pk>/delete/', views.del_group, name='del_group'),
    path('link/<int:pk>/new/', views.new_link, name='new_link'),
    path('link/<int:pk>/<int:g_pk>/delete/', views.del_link, name='del_link'),
    # path('group/link/', views.group, name='new_link')
]