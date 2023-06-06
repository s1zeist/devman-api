import requests

dict_option = {'key1': 'lang=ru&', 'key2': 'M&', 'key3': 'n&', 'key4': 'q&', 'key5': 'T'}
params = '?lang=ru&?M&?n&?q&?T'
cities = ['Шереметьево', 'Лондон', 'Череповец' + params]


def show_weather(city):
    url = f'https://wttr.in/{city}'
    response = requests.get(url)
    response.raise_for_status()
    return print(response.text)


for city in cities:
    show_weather(city)
