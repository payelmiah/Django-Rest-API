
from django.contrib import admin
from django.urls import path, include
from drapi import views
from rest_framework.routers import DefaultRouter
#create router object
router = DefaultRouter()
#register viewset with router
router.register('aiquest', views.Aiquest_model_view, basename='aiquest')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    #path('aiquest/', views.AiquestList_List_Create.as_view()),
    #path('aiquest/<int:pk>/', views.Aiquest_Retrieve_update_destroy.as_view()),
  

]

