from cgitb import text
import requests
'''
San Francisco
'''
url = 'https://wttr.in/san%20francisco?nTqu'
parameters = {
'lang': 'en'
}
response = requests.get(url, parameters)
response.raise_for_status()
# print(response.text)
'''
Для всех трех сразу
'''
raw = ['london','svo','cherepovets']
for i in raw:
  url_template = 'https://wttr.in/{}'
  url = url_template.format(i)
  parameters = {
    'lang': 'en'
  }
  if i == 'cherepovets':
    parameters = {
      'lang': 'ru',
      '?':'m'

    }
  response = requests.get(url, parameters)
  response.raise_for_status()
  print('\n\n', response.text, '\n')
'''
Moscow Sheremetievo
'''
url = 'https://wttr.in/svo'
parameters = {
'lang': 'en'
}
response = requests.get(url, parameters)
response.raise_for_status()
# print(response.text)
'''
London
'''
url = 'https://wttr.in/london'
parameters = {
'lang': 'en'
}
response = requests.get(url, parameters)
response.raise_for_status()
# print(response.text)
'''
Cherepovets
'''
url = 'https://wttr.in/cherepovets'
parameters = {
'lang': 'ru',
'?':'m'
}
response = requests.get(url, parameters)
response.raise_for_status()
# print(response.text)