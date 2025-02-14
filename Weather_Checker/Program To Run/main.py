#IMPORT SECTION

import requests
from config import get_weather

with open("creator_id.txt", "r") as creator_id:
    print(creator_id.read())

api_key = "input_your_api_key"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("INPUT CITY NAME: ")
result = get_weather(api_key=api_key, base_url=base_url, city=city)
print(result)


