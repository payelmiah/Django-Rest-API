
from django.contrib import admin
from django.urls import path, include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('aiquest/', views.aiquest_info),
    #path('aiquest/<int:pk>', views.aiquest_ins),
    path('ailist/', views.AiquestList.as_view(), name='ailist'),  #class based view for list
    path('aicreate/', views.AiquestCreate.as_view(), name='aicreate'),  #class based view for create
    path('airetrieve/<int:pk>/', views.AiquestRetrieve.as_view(), name='airetrieve'),  #class based view for retrieve
    path('aiupdate/<int:pk>/', views.AiquestUpdate.as_view(), name='aiupdate'),  #class based view for update
    path('aidelete/<int:pk>/', views.AiquestDelete.as_view(), name='aidelete'),  #class based view for delete
    #path('aicreate/<int:pk>', views.AiquestCreate.as_view(), name='aicreate'),
]

