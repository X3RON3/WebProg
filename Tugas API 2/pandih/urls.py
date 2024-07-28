from django.urls import path
from pandih import views
from pandih import views_api

app_name = 'pandih'
urlpatterns = [
   path('', views.readStudent, name='read-data-student'), 
   path('create/', views.createStudent, name='create-data-student'),   
   path('update/<str:id>', views.updateStudent, name='update-data-student'),   
   path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

   #Consume API
   path('api/get/', views_api.consumeApiGet, name='api-get'),
   path('api/add/', views_api.addData, name='api-add'),
   path('api/update/<int:user_id>/', views_api.updateData, name='api-update'),
]
