from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.docRoom, name='docRoom'),
    path('room/content/<str:id>/', views.docRoomContent, name='roomContent'),
    path('singleView/<str:pk>/', views.viewDoc, name='viewDoc'),
    path('create/', views.createDoc, name='createDoc'),
    path('', views.home, name='home'),
    path('edit/<str:id>/', views.editDoc, name='editDoc'),
]
