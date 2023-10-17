from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView

urlpatterns = [
    # Custom views
    #path("login/", views.user_login, name="login"),

    #default views
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change/done', PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('', include('django.contrib.auth.urls')),

    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

]
