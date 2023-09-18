from django.urls import path,include
from rest_framework import routers
from moviesandseries import views

router=routers.DefaultRouter()
router.register( r'movies', views.moviesViewSet ,basename='movies')
router.register(r'series' ,views.seriesViewSet,basename='series')

urlpatterns = [
    path('',include(router.urls))
]
