"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from book import views                                          # here we r importing the folder.
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.hompage, name="homepage"),
    path('show-all-Books/', views.show_all_books, name= "show_all_books"),
    path('edit/<int:id>/', views.edit_data, name="edit"),
    path('Delete/<int:id>/', views.Delete_data, name="Delete"),
    path('delete-all-books/', views.Delete_all_books, name="Delete_all_books"),
    path('soft-delete/', views.is_inactive, name="soft_delete"),
    path('update-soft-delete/<int:id>/', views.update_deleted_books, name="update-soft-delete"),
    path('restore-book/', views.restore_book, name="restore_book"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('form-home/', views.form_home, name="form_home"),
    
    
    path('home_cbv/', views.HomePage.as_view(), name="homepage"),
    path('template_cbv/', views.CBVTemplateView.as_view(), name="template_cbv"),

     path('', include(('book.urls'), namespace='book'))  
    # path('emp-gcreate/', views.EmployeeCreate.as_view(), name = 'EmployeeCreate'),  
    # path('emp-retr/', views.EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    # path('emp-retr/<int:pk>/', views.EmployeeDetail.as_view(), name = 'EmployeeDetail'),  
    # path('emp/<int:pk>/update/', views.EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    # path('emp/<int:pk>/delete/', views.EmployeeDelete.as_view(), name = 'EmployeeDelete'), 

    ]

# http://127.0.0.1:8000/emp-gcreate/
# http://127.0.0.1:8000/emp-retr/
# http://127.0.0.1:8000/emp-retr/2/



urlpatterns += [
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),

]





