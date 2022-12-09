from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.login_func, name="login_func"),
    path('loginout/', views.logout_func, name="logout_func"),
    path("register", views.register_request, name="register"),
]
