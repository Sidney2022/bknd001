from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from dotenv import load_dotenv
load_dotenv()
import os
import requests


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def index(request):
    visitor_name = request.GET.get('visitor_name', "Guest")
    user_ip = request.META.get('REMOTE_ADDR')
    location_response = requests.get(f'https://ipinfo.io/{user_ip}/json')
    data = location_response.json()
    city = data.get('city', "abuja")
    weather_resonsep = requests.get(f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}")
    weather = weather_resonsep.json()
    context = {
        "client_ip":user_ip,
        'location': city,
        "greeting": f"Hello {visitor_name}, the temperature is {weather['current']['temp_c']} degrees celcius in {city}.  You should expect/experience {weather['current']['condition']['text']}",
        "side_note":"city defaults to abuja if your location could not be determined"
    }
    
    return JsonResponse(context) 




