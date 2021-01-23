from rest_framework import serializers
from .models import Bucket, Game, StreamStat


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ['id', 'created_at']


class GameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = ['id', 'name']


class StreamStatSerializer(serializers.ModelSerializer):
    game_name = serializers.RelatedField(source='game', read_only=True)

    class Meta:
        model = StreamStat
        fields = ['id', 'game_name', 'data_type', 'value']
