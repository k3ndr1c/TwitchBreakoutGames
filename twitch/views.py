from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import (
    Bucket,
    Game,
    StreamStat,
)
from .serializers import (
    BucketSerializer,
    GameSerializer,
    StreamStatSerializer,
)

# Create your views here.


class BucketViewSet(viewsets.ModelViewSet):

    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class StreamStatViewSet(viewsets.ModelViewSet):

    queryset = StreamStat.objects.all()
    serializer_class = StreamStatSerializer