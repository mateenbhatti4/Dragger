from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login, name='admin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('all_users/',views.Users,name='all_users'),
    path('all_projects/',views.Projects,name='all_projects'),
    path('all_users/',views.Users,name='all_users'),
    path('profile_settings/',views.Profile,name='profile_settings'),
    path('all_payment/',views.Payment,name='all_payment'),
    path('admingallery/',views.gallery,name='admingallery'),
    path('logout/',views.Logout,name='logout'),

]
