from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Custom views
    #path("login/", views.user_login, name="login"),

    #default views
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),

    path('', include('django.contrib.auth.urls')),
    
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

]
