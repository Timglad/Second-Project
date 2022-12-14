from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.login_func, name="login_func"),
    path('loginout/', views.logout_func, name="logout_func"),
    path("register", views.register_request, name="register"),
    path('user/', views.user_menu, name="user"),
    path('showuser/', views.single_user, name="showuser"),
    path('firstlogin/', views.first_login, name="firstlogin"),
    path('customerlist/', views.customer_list, name="customerlist"),
    path('<pk>/deluser', views.deluser, name="deluser"),


]
