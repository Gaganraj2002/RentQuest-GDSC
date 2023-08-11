from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserView.as_view(), name="Home"),
    path("hello/", views.helloWorld.as_view(), name="Hello"),
]
