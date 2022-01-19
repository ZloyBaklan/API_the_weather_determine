import requests


def determining_weather(place):
    url_template = f'https://wttr.in/{place}'
    request_parameters = {
      'lang': 'ru',
      'm': '',
      'T': ''
    }
    response = requests.get(url_template, request_parameters)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['london', 'svo', 'cherepovets']
    for place in places:
        print('\n', determining_weather(place), '\n')
