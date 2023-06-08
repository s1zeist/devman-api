import requests

options = {'lang': 'ru&', '': 'M&n&q&T'}
cities = ['шереметьево', 'лондон', 'череповец']


def show_weather(city):
    params = '?lang=ru&?M&?n&?q&?T'
    url = f'https://wttr.in/{city}'
    if city == 'череповец':
        url += params

    response = requests.get(url, params=options)
    response.raise_for_status()
    return response.text


for city in cities:
    print(show_weather(city))
