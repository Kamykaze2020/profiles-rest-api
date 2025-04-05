from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    # standard function used to convert our api class view to be renderedby our urls.
    path('hello-view/', views.HelloApiView.as_view()),
    # it figures out the urls that are required for all of the functions that we add to our view set
    # and then it generates this 'urls' list which we can pass in to using the path function and the include function
    # to our url patterns
    # the reason we specify a black string '' is because we don't want to put a prefix to this url
    # we just want to include all of the urls in the base of this url's file
    path('', include(router.urls))
]
