# z pliku config.py zaimportuj strukturę Settings
# from datetime import datetime
import datetime
from tools import wind_speed
from tools import temp_c

from config import Settings
import requests

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Settings.city}&appid={Settings.api_key}"

    try:
        response = requests.get(URL)
        weather = response.json()

        data = {
            "Odczuwalna": temp_c(weather["main"]["feels_like"]),
            "Ciśnienie": weather["main"]["pressure"],
            "Wilgotność": weather["main"]["humidity"],
            "Zwykła temperatura": temp_c(weather["main"]["temp"]),
            "Opis pogody": weather["weather"][0]["description"],
            "Miejsce": weather["name"],
            "Prędkość wiatru": wind_speed(weather["wind"]["speed"]),
            # "Data pomiaru": datetime.fromtimestamp(weather["dt"]).strftime("%d/%m/%Y %H:%M:%S")
            "Data pomiaru": datetime.datetime.now()
        }
        return data

    except:
        print("Wystąpił błąd")

# print(fetch_weather())