from django.urls import path
from . import views

app_name = "loans"

urlpatterns = [    path('<pk>/loan',views.loans,name= 'loan'),
    path('loans/',views.loan_list_private,name= 'loans'),
    path('adminloans/',views.loan_list,name= 'adminloans'),
    path('lateloans/',views.late_loans,name= 'lateloans'),
    path('<pk>/latecheck',views.late_check,name= 'latecheck'),
    path('<pk>/return',views.returns,name= 'return'),

]
