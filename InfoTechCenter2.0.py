import random

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

# Call Functions Here
gasLevelAlert()


