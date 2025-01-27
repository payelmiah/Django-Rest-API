
from django.contrib import admin
from django.urls import path, include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('ailistcreate/', views.AiquestList_List_Create.as_view()),  #class based view for list
    
    path('airetrieve/<int:pk>/', views.Aiquest_Retrieve_update_destroy.as_view()),  #class based view for retrievew
  

]

