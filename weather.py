import requests
from config import API_KEY, BASE_URL
from datetime import datetime
from collections import defaultdict
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
        'units': 'imperial'
    }
    response = requests.get(f"{BASE_URL}/forecast", params=params)
    if response.status_code == 200:
        data = response.json()
        organized_data = defaultdict(lambda: {"entries": [], "min_temp": float('inf'), "max_temp": float('-inf')})

        for entry in data['list']:
            date = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
            hour = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S").strftime("%H:%M")

            temp = entry['main']['temp']
            organized_data[date]['min_temp'] = min(organized_data[date]['min_temp'], temp)
            organized_data[date]['max_temp'] = max(organized_data[date]['max_temp'], temp)
            
            # append weather info to date
            organized_data[date]['entries'].append({
                "time": hour,
                "temp": temp,
                "feels_like": entry['main']['feels_like'],
                "humidity": entry['main']['humidity'],
                "weather": entry['weather'][0]['description'],
                "wind_speed": entry['wind']['speed'],
                "wind_gust": entry['wind']['gust'] if 'gust' in entry['wind'] else None,
                "cloudiness": entry['clouds']['all'],
                "pop": entry['pop']
            })

        for date, data in organized_data.items():
            print(f"Date: {date}")
            print(f"  Min Temp: {data['min_temp']}°F")
            print(f"  Max Temp: {data['max_temp']}°F")
            for entry in data['entries']:
                print(f"    Time: {entry['time']}")
                print(f"      Temperature: {entry['temp']}°F (Feels like: {entry['feels_like']}°F)")
                print(f"      Humidity: {entry['humidity']}%")
                print(f"      Weather: {entry['weather']}")
                print(f"      Wind Speed: {entry['wind_speed']} m/s", end="")
                if entry['wind_gust']:
                    print(f" (Gusts: {entry['wind_gust']} m/s)")
                else:
                    print()
                print(f"      Cloudiness: {entry['cloudiness']}%")
                print(f"      Probability of Precipitation: {entry['pop']*100}%")
            print("\n")
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
    get_5_day_forecast(city)


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