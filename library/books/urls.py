from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("mains/", views.mains,name= "mains"),
    path("addbook/",views.add_book,name="addbook"),
    path("<pk>/delbook", views.delete_book,name="delbook"),
    path('<pk>/singlebook', views.single_book, name="single_book"),
    path('<pk>/edit', views.edit_book, name="edit"),
    path('searchbooks', views.search_books, name="searchbooks"),
    path("authors/", views.authors,name= "authors"),
    path("addauthor/",views.add_author,name="add_author"),
    path("<pk>/delauthor", views.delete_author,name="delete_author"),
    path('<pk>/singleauthor', views.single_author, name="single_author"),
    path('<pk>/editauthor', views.edit_author, name="edit_author"),
    path('searchbooks', views.search_books, name="searchbooks"),



]