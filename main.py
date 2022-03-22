import requests
from datetime import datetime
MY_LAT = 39.744431
MY_LONG = -75.545097
FORMATTED = 0


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

location = (longitude, latitude)
print(location)

parameters = {
    "latitude": MY_LAT,
    "longitude": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sun_data = response.json()
sunrise = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun_data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset, sunrise)

time_now = datetime.now()
print(time_now.hour)
