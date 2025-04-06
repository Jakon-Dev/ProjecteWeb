import requests

URL = 'https://valorant-api.com/v1/{}'

def get(endpoint):
    return requests.get(URL.format(endpoint)).json()

def get_agents():
    return get('agents')['data']

def get_maps():
    return get('maps')['data']

def get_cards():
    return get('playercards')['data']

def get_titles():
    return get('playertitles')['data']

