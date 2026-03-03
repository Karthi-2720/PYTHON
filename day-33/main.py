import requests

MY_LAT = 17.630222
MY_LONG = 78.484215
FORMATTED = 0
# x = requests.get(url="http://api.open-notify.org/iss-now.json")
# x.raise_for_status()
#
# data = x.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)
parameter ={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": FORMATTED,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)