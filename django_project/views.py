import requests
from django.shortcuts import render

def home(request):
  # Using APIs
  response =  requests.get("https://api.github.com/events")
  data = response.json()
  result = data[0]["repo"]

  response = requests.get("https://dog.ceo/api/breeds/image/random") 
  data2 = response.json()
  result2 = data2["message"] 
  return render(request, "templates/index.html", {"result": result, "result2": result2})