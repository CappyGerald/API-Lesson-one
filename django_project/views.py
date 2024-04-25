import requests
from django.shortcuts import render

def home(request):
  # Using APIs
  api_key = '91ba82a5d5741658679706ec974cadb4'
  city = 'Nairobi'

  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)
  data = response.json()


  weather = {
    'city': city,
    'temperature': round(data['main']['temp'] - 273.15, 2), # I want the temperature in celsius roundeff of to 2dp
    'description': data['weather'][0]['description'],
    'icon': data['weather'][0]['icon']
  }

  return render(request, 'templates/index.html', {'weather': weather})