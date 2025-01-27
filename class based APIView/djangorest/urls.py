
from django.contrib import admin
from django.urls import path, include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('aiquest/', views.aiquest_info),
    #path('aiquest/<int:pk>', views.aiquest_ins),
    path('aicreate/', views.AiquestCreate.as_view(), name='aicreate'), 
    path('aicreate/<int:pk>', views.AiquestCreate.as_view(), name='aicreate'),
]

