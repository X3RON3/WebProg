from django.urls import path
from pandih import views
from pandih import views_api

app_name = 'pandih'
urlpatterns = [
   path('', views.home, name='read-data-student'),  
   path('', views.readStudent, name='read-data-student'),   
   path('create/', views.createStudent, name='create-data-student'),   
   path('update/<str:id>', views.updateStudent, name='update-data-student'),   
   path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

   #buat course
   path('read/course', views.readCourse, name='read-data-course'),
   path('delete/<str:id>', views.deleteCourse, name='delete-data-course'),

   path('api/course', views_api.apiCourse, name='api-view-data-course'),
]
