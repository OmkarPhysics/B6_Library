from django.urls import path  
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete



app_name = 'book'  
urlpatterns = [  
    path('emp-gcreate/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),  
    path('emp-retr/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('emp-retr/<int:pk>/', EmployeeDetail.as_view(), name = 'EmployeeDetail'),   
    path('emp/<int:pk>/update/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('emp/<int:pk>/delete/', EmployeeDelete.as_view(), name = 'EmployeeDelete'),  
  
]  