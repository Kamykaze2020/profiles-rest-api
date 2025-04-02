from django.urls import path
from profiles_api import views

urlpatterns = [
    # standard function used to convert our api class view to be renderedby our urls.
    path('hello-view/', views.HelloApiView.as_view()),
]
