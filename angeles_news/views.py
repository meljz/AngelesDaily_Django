from django.http import HttpResponse
from django.shortcuts import render
import requests

# weather API is within the home function, since the weather is within the home.html
#home page function
def home (request):
    city = "Angeles City"
    api_key = "ecd99d160a29b035f2e1c8116aab69f3" #api key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url) #requestiong api 
        data = response.json()       #converting API into json
       
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        
    except Exception as e:          # will fire once above fails
        print ("weather error", e)
        weather = None
    
    return render (request, "home.html", {"weather": weather}) #passing data into home.html "{weather": weather}"

#about page function
def about (request):
    return render (request, "about.html")
   