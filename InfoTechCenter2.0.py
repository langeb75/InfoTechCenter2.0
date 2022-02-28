# Code Name - Hornet

# Import Libraries Here
from time import sleep  #Print to one line with time delay between prints

import colorama
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

import random

# Welcome Branch

print(Fore.BLUE + "Welcome to Hornets InfoTechCenter\n")

sleep(1)

print(Fore.BLUE + "Hornet's Operating System Booting Up\n")

sleep(1)


# Gas Branch

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

# Create IF-ELIF-ELSE statements using the Comparative Operator == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1,25),1)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***\nYour gas tank is extremely LOW\nThe closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away!")
    elif gasLevelIndicator == "Quarter Tank":
        print("You are on a QUARTER TANK of gas\nStart planning a visit to the gas station!!!")
    elif gasLevelIndicator == "Half Tank":
        print("You have a HALF TANK of gas\nYou have 125 more miles to empty!!!!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You have THREE QUARTER TANK of gas\nYou have 205 more miles to empty!!!!")
    else:
        print("You have a FULL TANK of gas, Congratulations.\nYou have 310 more miles to empty!!!!")


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

# Call Functions Here
gasLevelAlert()
vehicleResponseSystem()

