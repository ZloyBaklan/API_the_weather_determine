import requests


def weather_in_town(places):
  for i in places:
    url_template = f'https://wttr.in/{i}'
    request_parameters = {
      'lang': 'ru',
      'F': 'm'
    }
    response = requests.get(url_template, request_parameters)
    response.raise_for_status()
    print('\n\n', response.text, '\n')

if __name__ == '__main__':
  places = ['london','svo','cherepovets']
  weather_in_town(places)
