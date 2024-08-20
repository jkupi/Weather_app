import requests
from config import API_KEY, BASE_URL
# import socket

def get_current_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'
    }

    response = requests.get(f"{BASE_URL}/weather", params=params)

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
    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(f"{BASE_URL}/weather", params=params)
    if response.status_code == 200:
        data = response.json()
        return data['coord']['lat'], data['coord']['lon']
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def get_5_day_forecast(city):
    lat, lon = get_city_coordinates(city)
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(f"{BASE_URL}/forecast", params=params)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        return None

def get_uv_index(city):
    lat, lon = get_city_coordinates(city)
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY
    }
    response = requests.get(f"{BASE_URL}/uvi", params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"UV Index = {data['value']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def generate_report(city):
    ""


if __name__ == "__main__":
    city = "lagrange"
    # get_current_weather(city)
    # get_uv_index(city)
    # get_city_coordinates(city)
    # get_5_day_forecast(city)


    """
    try:
        host = 'api.openweathermap.org'
        print(f"IP address of {host}: {socket.gethostbyname(host)}")
    except socket.gaierror as e:
        print(f"Error resolving {host}: {e}")
        


city_name = 'Lagrange'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'    
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')
"""