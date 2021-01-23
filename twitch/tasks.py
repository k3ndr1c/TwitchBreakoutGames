import datetime
import celery
import TwitchApi


def isBreakoutGame(viwer_count, active_channels):
    """Calculation if game is important"""
    
    return True


# Scheduling cron jobs that run every 5 minutes
# https://django.cowhite.com/blog/scheduling-taks-in-django/
@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
def create_new_timebucket():

    # Create new bucket
    bucket = Bucket.objects.create()

    # Get access token
    access_token = TwitchApi.get_access_token()


    # Get important game list
    games = [('test', 25000)]

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
    

