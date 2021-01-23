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


class StreamStatViewSet(viewsets.ModelViewSet):

    queryset = StreamStat.objects.all()
    serializer_class = StreamStatSerializer

    def get_queryset(self):
        user = self.request.user
        bucket = Bucket.objects.latest('created_at')
        return StreamStat.objects.filter(bucket=bucket)
