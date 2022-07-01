from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', auth_view.LoginView.as_view(template_name='users/CV.html'), name='cv'),
    path('createcv/', auth_view.LoginView.as_view(template_name='users/createcv.html'), name='createcv'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('CV/', auth_view.LoginView.as_view(template_name='users/CV.html'), name="CV")
]
