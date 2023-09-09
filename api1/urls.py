from django.urls import path
from .views import *
urlpatterns = [
    path('item/',ItemList.as_view()),     #nestaamlo as_view khaterha class not a function
    path('item/<int:pk>/',ItemDetail.as_view()),
    path('location/',LocationList.as_view()),
    path('location/<int:pk>/',LocationDetail.as_view()),
 
]
