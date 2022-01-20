import requests


def determine_weather_forecast(place):
    url_template = f'https://wttr.in/{place}'
    request_parameters = {
      'lang': 'ru',
      'm': '',
      'T': '',
      'n':'',
      'q':''
    }
    response = requests.get(url_template, request_parameters)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    places = ['london', 'svo', 'cherepovets']
    for place in places:
        print('\n', determine_weather_forecast(place), '\n')
