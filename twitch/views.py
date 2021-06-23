from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import (
    Bucket,
    StreamStat,
)
from .serializers import StreamStatSerializer

# Create your views here.


class StreamStatViewSet(viewsets.ModelViewSet):

    queryset = StreamStat.objects.all()
    serializer_class = StreamStatSerializer

    def get_queryset(self):
        return StreamStat.objects.all()
        # user = self.request.user
        # bucket = Bucket.objects.latest('created_at')
        # return StreamStat.objects.filter(bucket=bucket)


