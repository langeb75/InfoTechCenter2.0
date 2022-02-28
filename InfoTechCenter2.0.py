import random

# Weather Branch

def weather():
    weatherForecast = ["Icy","Snowy","Raining","Windy","Foggy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather Function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forcast of",weatherAlert,":(")
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snowy":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Raining":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    else:
        print("\nWeather is",weatherAlert,"let's GOOOOOOOOOOOO")
        print("VRS will allow your car to go 120MPH")

vehicleResponseSystem()

