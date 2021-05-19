# import requests
#
# res = requests.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()
#
# data = res.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_poss = (longitude, latitude)
#
# print(iss_poss)

# when is the sun going up or down?
from datetime import datetime

import requests

MY_LAT = 52.070499
MY_LONG = 4.300700

param = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

res = requests.get("https://api.sunrise-sunset.org/json", params=param)
res.raise_for_status()
data = res.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # getting the actual hour
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]  # getting the actual hour

print(sunset)
print(sunrise)

time_now = datetime.now()
