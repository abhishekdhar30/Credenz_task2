from django.urls import path
from . import views


urlpatterns = [
    path('',views.register,name='register'),
    path('dev/',views.dev,name='dev'),
    path('in/log/',views.push,name="push"),
]