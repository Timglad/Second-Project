from django.urls import path
from . import views,entry

app_name = "books"

urlpatterns = [
    path("mains/", views.mains,name= "mains"),
    path("addbook/",views.add_book,name="addbook"),
    path("<pk>/delbook", views.delete_book,name="delbook"),
    path('<pk>/singlebook', views.single_book, name="single_book"),
    path('<pk>/edit', views.edit_book, name="edit"),
    path('login/', entry.login_func, name="login_func"),
    path('loginout/', entry.logout_func, name="logout_func"),
    path('register/', entry.register_func, name="register_func"),
    path('searchbooks', views.search_books, name="searchbooks")
]