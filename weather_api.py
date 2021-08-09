import requests
from config import WEATHER_APP_ID


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_APP_ID}'
    data = requests.get(url).json()
    code = data["cod"]
    if code == '404':
        return 'City not found!'
    else:
        citi = data["name"]
        main = data["weather"][0]["main"]
        temp = int(data["main"]["temp"]) - 273
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        info = f'{citi}\n{main}\nTemperature: {temp}\nWind: {wind}\nH: {humidity}%'
        return info


