#home_URLS.py

from django.urls import path
from api.views import home_views as views 


urlpatterns = [
   path('', views.home, name='home'),
   path('create', views.create_todo, name='create_todo'), 
   path('complete/<int:todo_id>', views.complete_todo, name='complete_todo'),
   path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
 
]