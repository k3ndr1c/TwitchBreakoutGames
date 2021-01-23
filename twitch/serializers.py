from rest_framework import serializers
from .models import Bucket, Game, StreamStat

# Create your serializers here.


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ['id', 'created_at']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name']


class StreamStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamStat
        fields = ['id', 'game', 'bucket', 'data_type', 'value']
