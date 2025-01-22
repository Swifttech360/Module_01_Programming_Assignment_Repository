#Assignment Part I:

#Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is as follows:  F=9/5*C+32

#The program should ask the user to enter a temperature in Celsius, then display the temperature converted to
# Fahrenheit. (15 points)
while True:
    try:
        unformattedC = float(input('Enter Celsius temp to convert to Fahrenheit: \n'))
    except ValueError:
        print('Invalid input \nPlease try again.\n')
        continue
    unformattedF = (unformattedC)
        #(9/5 * celsius + 32)


    fahrenheit = (
f"{unformattedF:.0f}" if unformattedF % 1 == 0
 else f"{unformattedF:.1f}" if round(unformattedF % 1, 1) == unformattedF  % 1
  else f"{unformattedF:.0f}" if round(unformattedF % 1, 4) == unformattedF % 1
   else f"{unformattedF:.2f}")

    celsius = f"{unformattedC:.0f}" if unformattedC % 1 == 0 else unformattedC



    print(f'\n{unformattedC:.2f}ºC is equal to {fahrenheit}ºF')
