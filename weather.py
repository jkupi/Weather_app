import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    ""

def get_city_coordinates(city):
    ""


city_name = 'Lagrange'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'    
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')