from multiprocessing import context
from multiprocessing.sharedctypes import Value
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=pt_br&appid=eda1006b74de80cbb8fdbbb51367068e'
    city= 'Curitiba'

    if request.method == 'POST':
        form = CityForm(request.POST)
       

    form = CityForm()


    cities = City.objects.all()

    weather_data = []

    for city in cities:
        
        r =  requests.get(url.format(city)).json()
        
        city_weather = {
        'city' : city.name,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    
    }

        weather_data.append(city_weather)
    context = {'weather_data' : weather_data, 'form' : form}
    print (weather_data)

    
    return render(request, 'weather/weather.html',context)
    


