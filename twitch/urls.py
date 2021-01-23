from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'twitch'

router = DefaultRouter()
router.register(r'stream-stats', views.StreamStatViewSet, basename='stream-stat')


urlpatterns = [
    path('', include(router.urls))
]
