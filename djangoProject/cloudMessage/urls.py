from django.urls import path
from cloudMessage import views

urlpatterns = [
    path('', views.hello),
    path('msg', views.msgproc),
]
