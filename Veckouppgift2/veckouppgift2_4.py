#Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
#Version 1, exempel på output:
from contextlib import nullcontext
from string import printable

from wheel.cli.convert import convert

#Skriv in en temperatur i grader Celsius: 22
##Det blir 71.6 grader Fahrenheit.

#Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
##Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit. Använd sedan if + else.

##Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

#Formel för konvertering mellan temperaturenheter:
#C = (F - 32) / 1.8
#F = 1.8 * C + 32

#Förslag på värden att testa med:

## Programmet fråga användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen
temp_in_celsius = 0
temp_in_fahrenheit = 0
temp_measurement_scale = 0

print(" Input value must be '1' or '2'")
while True:
    try:
         temp_measurement_scale = int (input(" Please input '1' for Celsius and '2' for Fahrenheit: "))
         if  temp_measurement_scale != 2 and temp_measurement_scale != 1 and temp_measurement_scale == nullcontext:
             print(" Please input value '1' for Celsius or '2' for Fahrenheit")
             continue
         break
    except ValueError:
        print("Only whole numbers are acceptable!")

if temp_measurement_scale == 1:
        celsius_input_value = float (input("Please input temperature in Celsius: "))
        temp_in_fahrenheit = 1.8 * celsius_input_value + 32
        print("Temperature in Fahrenheit is ",(round (temp_in_fahrenheit,4)), " degree Fahrenheit" )

elif temp_measurement_scale == 2:
        fahrenheit_input_value = float (input("Please input temperature in Fahrenheit: "))
        temp_in_celsius = (fahrenheit_input_value - 32) / 1.8
        print("Temperature in Celsius is ", (round(temp_in_celsius,4)), "degree celsius")
        if temp_in_celsius < 10:
            print("The temperature is ", (round(temp_in_celsius,4)), "degree celsius. Please put on a winter jacket!")
        elif temp_in_celsius >= 20:
            print("The temperature is ", (round(temp_in_celsius,4)), "degree celsius. Please put your winter jacket in the closet! ")
