import datetime
# from celery import shared_task
from app.celery import app
from django.conf import settings
from twitch import TwitchApi, TwitchScrape
from twitch.models import Bucket, Game, StreamStat



def isBreakoutGame(viewer_count, active_channels):
    """Calculation if game is important"""
    # Temp metrics
    if (50001 <= viewer_count < 100000) and (active_channels >= 20):
        return True
    else:
        return False

# Scheduling cron jobs that run every 5 minutes
# https://django.cowhite.com/blog/scheduling-taks-in-django/
# @celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
# @shared_task
@app.task
def create_new_timebucket():
    print("made it.")
    # Create new bucket
    bucket = Bucket.objects.create()
    print("bucket")
    # Get access token
    access_token = TwitchApi.get_access_token()
    # Get important game list
    games = TwitchApi.get_games(0, access_token)
    data = []
    for name, _ in games:
        game = Game.objects.get_or_create(name=name)
        print(game)
        # Query stream summary
        active_channels, viewer_count = TwitchApi.get_stream_summary(name, access_token)
        data.append((game, name, viewer_count, active_channels))
        print(data)
    # Process data and filter out which are important
    for game, name, viewer_count, active_channels in data:

        if isBreakoutGame(viewer_count, active_channels):
            # Add stream data for viewcount and channels
            print("breakout!")
            stream_stat = StreamStat.objects.create(game=game[0], bucket=bucket, data_type='viewcount', value=viewer_count)
            stream_stat = StreamStat.objects.create(game=game[0], bucket=bucket, data_type='channels', value=active_channels)

