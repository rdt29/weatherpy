  
import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

x= open("weather.txt" , 'w')

print ("-------------------------------------------------------------",file=x)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file=x)
print ("-------------------------------------------------------------",file=x)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file=x)
print ("Current weather desc  :",weather_desc,file=x)
print ("Current Humidity      :",hmdt, '%',file=x)
print ("Current wind speed    :",wind_spd ,'kmph',file=x)

