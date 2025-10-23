from django.http import HttpResponse
from django.shortcuts import render
import requests
from newsapp.models import Articles

# weather API is within the home function, since the weather is within the home.html
#home page function
def home (request):
    #fetch api weather start (i putted it a specific box in home.html)----------
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
    #fetch api weather end-=---------------------------
    
    #just like in news app, im using the newsapp article to pass the data into the home.html in a specific box
    articles = Articles.objects.all().order_by('-created_at')
    return render(request, 'home.html', {
                  'articles': articles,
                  "weather": weather})  #passing data into home.html "{weather": weather}" and "{'articles': articles}"




#about page function
def about (request):
    return render (request, "about.html")
   