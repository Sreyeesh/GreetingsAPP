import tkinter as tk
from geopy.geocoders import Nominatim
import pycountry
import time
import datetime

def greet():
    name = name_entry.get()
    location_name = location_entry.get()

    geolocator = Nominatim(user_agent="greeting_app")
    location = geolocator.geocode(location_name)

    country_code = location.raw.get("address", {}).get("country_code", "")
    if country_code:
        country = pycountry.countries.get(alpha_2=country_code)
        language_code = country.languages[0].iso639_1
        language = pycountry.languages.get(iso639_1=language_code).name
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        location = geolocator.reverse(f"{location.latitude}, {location.longitude}", exactly_one=True)
        country_code = location.raw.get("address", {}).get("country_code", "")
        country = pycountry.countries.get(alpha_2=country_code)
        language_code = country.languages[0].iso639_1
        language = pycountry.languages.get(iso639_1=language_code).name

    if language == "English":
        greeting = f"Hello, {name} from {location_name}!"
    elif language == "German":
        greeting = f"Hallo, {name} aus {location_name}!"
    elif language == "Spanish":
        greeting = f"Hola, {name} de {location_name}!"
    else:
        greeting = f"Hello, {name} from {location_name} in {language}!"

    greeting_label.config(text=greeting)

root = tk.Tk()
root.tk.call('tk', 'scaling', 4.0)
root.title("Greeting App")

name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)

location_label = tk.Label(root, text="Enter your location:")
location_entry = tk.Entry(root)

greeting_button = tk.Button(root, text="Greet", command=greet)
greeting_label = tk.Label(root, text="")

name_label.pack()
name_entry.pack()
location_label.pack()
location_entry.pack()
greeting_button.pack()
greeting_label.pack()

root.mainloop()
