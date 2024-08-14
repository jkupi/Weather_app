import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# fetch API key
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
