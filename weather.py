import requests
from config import API_KEY, BASE_URL

def get_current_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']

        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°F")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return None
    
def get_city_coordinates(city):
    ""

def get_forecast(city):
    ""

def get_uv_index(lat, lon):
    ""

def generate_report(city):
    ""


if __name__ == "__main__":
    city = "Lagrange"
    get_current_weather(city)


""""
city_name = 'Lagrange'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'    
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')
    """