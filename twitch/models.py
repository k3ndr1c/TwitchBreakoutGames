from django.db import models


class Bucket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Game(models.Model):
    name = models.CharField(required=True, max_length=255)

    def __str__(self):
        return str(self.name)


class StreamStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    data_type = models.CharField(blank=True, max_length=255)
    value = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f'{self.data_type}, {self.value}'
