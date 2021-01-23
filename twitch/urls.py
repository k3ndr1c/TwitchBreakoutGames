from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'twitch'

urlpatterns = [
    # path('get-streams', views.StreamStatsRetrieve.as_view(), name='create'),
]
