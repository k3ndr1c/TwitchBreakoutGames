import datetime
from celery import shared_task
from django.conf import settings
from twitch import TwitchApi, TwitchScrape
from .models import Bucket, Game, StreamStat
from app.celery import app


def isBreakoutGame(viewer_count, active_channels):
    """Calculation if game is important"""
    # Temp metrics
    if (500 <= viewer_count < 5000) and (active_channels >= 20):
        return True
    else:
        return False

# Scheduling cron jobs that run every 5 minutes
# https://django.cowhite.com/blog/scheduling-taks-in-django/
# @celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
@shared_task
def create_new_timebucket():
    print("made it.")
    # Create new bucket
    bucket = Bucket.objects.create()
    # Get access token
    access_token = TwitchApi.get_access_token()
    # Get important game list
    games = TwitchScrape.scrape()
    data = []
    for name, _ in games:
        if not Game.objects.filter(name=name).exists():
            game = Game.objects.create()
        else:
            game = Game.objects.all().filter(name=name)

        # Query stream summary
        active_channels, viewer_count = TwitchApi.get_stream_summary(name, access_token);
        data.append((game, name, viewer_count, active_channels))

    # Process data and filter out which are important
    for game, name, viewer_count, active_channels in data:

        if isBreakoutGame(viewer_count, active_channels):
            # Add stream data for viewcount and channels
            stream_stat = StreamStat.objects.create(game=game, name=name, type='viewcount', value=viewer_count)
            stream_stat = StreamStat.objects.create(game=game, name=name, type='channels', value=active_channels)

app.conf.beat_schedule = {
    "run-me-every-minute": {
    "task": "tasks.check",
    "schedule": 60.0
    }
}
