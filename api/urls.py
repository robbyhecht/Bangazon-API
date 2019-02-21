from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
#first movies for route, second movies for naming convention('movies, views.MovieViewSet, 'movies')
router.register('customers', views.CustomerViewSet)
router.register('producttype', views.ProductTypeViewSet)
# router.register('directors', views.DirectorViewSet)
# router.register('actors', views.ActorViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
]