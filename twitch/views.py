from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import (
    Bucket,
    StreamStat,
    Game,
)
from .serializers import (
    StreamStatSerializer,
    GameSerializer,
)

# Create your views here.


class StreamStatViewSet(viewsets.ModelViewSet):
    # queryset = StreamStat.objects.filter(bucket=latest)
    queryset = StreamStat.objects.all()
    serializer_class = StreamStatSerializer

    def get_queryset(self):
        # return StreamStat.objects.all()
        # user = self.request.user
        bucket = Bucket.objects.latest('created_at')
        return StreamStat.objects.filter(bucket=bucket)


class GameViewSet(viewsets.ModelViewSet):
    latest = Bucket.objects.all()
    queryset = Game.objects.all()
    serializer_class = GameSerializer

