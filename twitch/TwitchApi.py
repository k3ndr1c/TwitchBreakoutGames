import requests
from django.conf import settings

# client api information
client_id = settings.CLIENT_ID
client_secret = settings.CLIENT_SECRET


def get_access_token():
    """Returns the bearer token for authentication to use Twitch API"""

    app_access_url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
        'scope': []
    }
    token_request = requests.post(app_access_url, data)
    data = token_request.json()
    access_token = data['access_token']
    expires_in = data['expires_in']
    token_type = data['token_type']

    return access_token

def get_stream_summary(game_name, access_token):
    """Given a game, return the number of active channels streaming and current total viewercount"""

    url = 'https://api.twitch.tv/kraken/streams/summary/'
    payload = {
        'game': game_name.lower()
    }
    headers = {
    'client-id': client_id,
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/vnd.twitchtv.v5+json'
    }
    r = requests.get(url, params=payload, headers=headers)
    data = r.json()

    active_channels = data['channels']
    viewers = data['viewers']

    return active_channels, viewers

def get_live_streams(game_name, access_token, limit=5):
    """Gets information of the top viewed streamers of the input game"""

    url = 'https://api.twitch.tv/kraken/streams/'
    payload = {
        'game': game_name,
        'limit': limit
    }
    headers = {
    'client-id': client_id,
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/vnd.twitchtv.v5+json'
    }
    r = requests.get(url, params=payload, headers=headers)
    data = r.json()['streams']

    return data

def get_games(offset, access_token, limit=100):
    """Gets information of the top streamed games"""

    url = 'https://api.twitch.tv/kraken/games/top'
    payload = {
        'limit': limit,
        'offset': offset
    }
    headers = {
    'client-id': client_id,
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/vnd.twitchtv.v5+json'
    }
    r = requests.get(url, params=payload, headers=headers)
    data = r.json()['top']
    games = []
    for game in data:
        viewers = int(game['viewers'])
        if viewers < 50000:
            return games
        name = game['game']['name']
        games.append((name, viewers))
    if games[-1][1] > 50000:
        games.extend(get_games(offset + limit, access_token, limit))
    return games

