import requests
import urllib.parse


# client api information
client_id = 'vady69007xdupx60w6op78bq4dh8nd'
client_secret = 'vk510dzemn9mym6fl5m5v1c03z6szf'

# getting bearer token
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



# Example search query
url = 'https://api.twitch.tv/helix/search/channels'
payload = {
    'query': 'a_seagull'
}
headers = {
    'client-id': client_id,
    'Authorization': f'Bearer {access_token}',
}
r = requests.get(url, params=payload, headers=headers)

data = r.json()['data'][0]

# for key, value in data.items():
#     print(f'{key}, {value}')


# Example get live streams

url = 'https://api.twitch.tv/kraken/streams/'
payload = {
    'game': 'Overwatch'
}
headers['Accept'] = 'application/vnd.twitchtv.v5+json'
r = requests.get(url, params=payload, headers=headers)
data = r.json()['streams']

# print(data[0])


# Example live stream summary
url = 'https://api.twitch.tv/kraken/streams/summary/'
payload = {
    'game': 'summoners war: sky arena'
}
headers['Accept'] = 'application/vnd.twitchtv.v5+json'
r = requests.get(url, params=payload, headers=headers)
data = r.json()

print(data)



# url template for game pictures
game_name = 'StarCraft II'
game_name = urllib.parse.quote(game_name)
url = f'https://static-cdn.jtvnw.net/ttv-boxart/{game_name}-272x380.jpg'

print(url)