from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', views.HomeView.as_view(),name = 'home'),
  path('login', views.LoginInterfaceView.as_view(),name ='login'),
  path('signup', views.signup,name ='signup'),
  path('logout', views.logout,name ='logout'),
]
