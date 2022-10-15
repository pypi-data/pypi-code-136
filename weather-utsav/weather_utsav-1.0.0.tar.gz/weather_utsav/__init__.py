import requests
import json

part='minutely,hourly'
api_key='3ef770c5bde684b66dbc2a7537492d9c'






class WeatherProvider:
    def __init__(self,latitude,longitude):
        self.latitude=latitude
        self.longitude=longitude

    def getTodayWeather(self):
        currentWeather_api_address=f'https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&exclude={part}&appid={api_key}'
        res=requests.get(currentWeather_api_address).json()
        weather={
            "temp":round(res['current']['temp']-273.15,2),
            "humidity":res['current']['humidity'],
            "sky":res['current']['weather'][0]['description'],
            "weather_icon":res['current']['weather'][0]['icon']
        }
        return weather
    
    def getForecastWeather(self):
        currentWeather_api_address=f'https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&exclude={part}&appid={api_key}'
        res=requests.get(currentWeather_api_address).json()
        humd = []
        days = []
        night = []
        overallTemp = []
        description = []
        icons=[]
        for i in res["daily"]:
            humd.append(i['humidity'])
            days.append(round(i['temp']['day'] - 273.15, 2))
            night.append(round(i['temp']['night'] - 273.15, 2))
            description.append(i['weather'][0]['main'] + ": " + i['weather'][0]['description'])
            icons.append(i['weather'][0]['icon'])

        for i in range(len(days)):
            overallTemp.append(round((days[i] + night[i]) / 2, 2))

        weather={
            "temperature of days":days,
            "temperature of nights":night,
            "average temperature":overallTemp,
            "humidity":humd,
            "sky":description,
            "weather_icon":icons
        }
        return weather








