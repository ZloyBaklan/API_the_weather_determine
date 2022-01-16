from cgitb import text
import requests

'''
Для всех трех сразу
'''
RAW = ['london','svo','cherepovets']
for i in RAW:
  url_template = 'https://wttr.in/{}'
  url = url_template.format(i)
  parameters = {
    'lang': 'ru',
    '?': 'm'
  }
  response = requests.get(url, parameters)
  response.raise_for_status()
  print('\n\n', response.text, '\n')
