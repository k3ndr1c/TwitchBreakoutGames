from django.contrib import admin

# Register your models here.
from .models import Bucket, Game, StreamStat

admin.site.register(Bucket)
admin.site.register(Game)
admin.site.register(StreamStat)
