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
    path("register", entry.register_request, name="register"),
    path('searchbooks', views.search_books, name="searchbooks"),
    path('<pk>/loan',views.loans,name= 'loan'),
    path('loans/',views.loan_list,name= 'loans'),
    path('<pk>/return',views.returns,name= 'return')

]