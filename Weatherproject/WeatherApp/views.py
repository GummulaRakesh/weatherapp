# weather_app/views.py

from django.shortcuts import render
import requests


def weather_view(request):
    weather_data = {}
    if 'city' in request.POST:
        city = request.POST['city']
        api_key = '59c4b1fc89da41af6008e25b721b6d54'  # Replace with your actual OpenWeatherMap API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            # print("everything is fine")
            data = response.json()
            degree=data['wind']['deg']
            Direction=[]
            if degree >= 315 and degree <= 45:
                Direction.append('N')
            elif degree > 45 and degree <= 135:
                Direction.append('E')
            elif degree > 135 and degree <= 225:
                Direction.append('S')
            else:
                Direction.append('W')
            # print(Direction[0])

            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like' :data['main']['feels_like'],
                'Humidity' : data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'speed': data['wind']['speed'],
                # 'deg' : data['wind']['deg'],
                'direction' : Direction[0],
                'icon': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png",
            }
            # print('description', data['weather'][0]['description'])
        else:
            # print("issue with if")
            weather_data['error'] = 'City not found'

    return render(request, 'Weather.html' ,{'weather_data':weather_data})
