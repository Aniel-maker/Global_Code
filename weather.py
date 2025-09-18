from pyowm.owm import OWM
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key")
location = input('Enter your location')
owm = OWM(api_key)
weather_mgr = owm.weather_manager ()
observation = weather_mgr.weather_at_place(location)
w = observation.weather

weather_staus = w.detailed_status
weather_wind = w.wind()['speed']
weather_humidity = w.humidity
weather_temperature = w.temperature('celsius')['temp']

name = 'Agormeda Nathaniel Tetteh'
age = 19
forecast = f"My name is {name}. I am {age} years old. For today's weather in {location}, we have {weather_staus}. The wind is recorded to be moving at the velocity of {weather_wind} km/h. The humidity is {weather_humidity} m^3 and the temperature is {weather_temperature} degree. Have a lovely day."
print(forecast)