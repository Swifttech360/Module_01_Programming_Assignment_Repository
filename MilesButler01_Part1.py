#Author: Miles Butler
#Date written: 1/22/25
#Python Interpreter: IDLE version 3.13
#Assignment:Module 01 Programming Assignment
#Summary: This is a Python program that gets a Celsius temperature from the user, then uses a formula to convert it
# to Fahrenheit.
while True:
    try:
        unformattedC = float(input('Enter Celsius temp to convert to Fahrenheit: \n'))
    except ValueError:
        print('Invalid input \nPlease try again.\n')
        continue
    unformattedF = (9/5 * unformattedC + 32)


    fahrenheit = (
f"{unformattedF:.0f}" if unformattedF % 1 == 0
 or round(unformattedF % 1, 2) == 0
  else f"{unformattedF:.1f}" if round(unformattedF % 1, 1) == unformattedF % 1
   or round(unformattedF % 1, 2) == round(unformattedF % 1, 1)
    else f"{unformattedF:.2f}")

    celsius = f"{unformattedC:.0f}" if unformattedC % 1 == 0 else unformattedC
    
    print(f'\n{celsius}ºC is equal to {fahrenheit}ºF')
