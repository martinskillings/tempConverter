
#Write a program that converts Celsius to Fahrenheit or Kelvin

continueLoop = 'f'

while continueLoop == 'f':

    celsius = eval(input("Enter a degree in Celsius: "))
    fahrenheit = (9 / 5 * celsius + 32)
    
    print(celsius, "Celsius is", format(fahrenheit, ".2f"), "Fahrenheit")

    #User prompt to switch to different temperature setting or terminate program
    continueLoop = input("Enter f to continue in Fahrenheit, k to change to Kelvin, or q to quit: ")

    if continueLoop == 'k':
        
        celsius = eval(input("Enter a degree in Celsius: "))
        kelvin = celsius + 273.15

        print(celsius, "Celsius is", format(kelvin, ".2f"), "Kelvin")

        continueLoop = input("Enter f to go back to Fahrenheit, k to stay in Kelvin, or q to quit: ")
        
    if continueLoop == 'q':

        print ("Good-Bye")


'''
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/marti/AppData/Local/Programs/Python/Python36-32/tempConverter.py 
Enter a degree in Celsius: 43
43 Celsius is 109.40 Fahrenheit
Enter f to continue in Fahrenheit, k to change to Kelvin, or q to quit: k
Enter a degree in Celsius: 43
43 Celsius is 316.15 Kelvin
Enter f to go back to Fahrenheit, k to stay in Kelvin, or q to quit: f
Enter a degree in Celsius: 0
0 Celsius is 32.00 Fahrenheit
Enter f to continue in Fahrenheit, k to change to Kelvin, or q to quit: k
Enter a degree in Celsius: 0
0 Celsius is 273.15 Kelvin
Enter f to go back to Fahrenheit, k to stay in Kelvin, or q to quit: f
Enter a degree in Celsius: 100
100 Celsius is 212.00 Fahrenheit
Enter f to continue in Fahrenheit, k to change to Kelvin, or q to quit: k
Enter a degree in Celsius: 100
100 Celsius is 373.15 Kelvin
Enter f to go back to Fahrenheit, k to stay in Kelvin, or q to quit: f
Enter a degree in Celsius: 37
37 Celsius is 98.60 Fahrenheit
Enter f to continue in Fahrenheit, k to change to Kelvin, or q to quit: k
Enter a degree in Celsius: 37
37 Celsius is 310.15 Kelvin
Enter f to go back to Fahrenheit, k to stay in Kelvin, or q to quit: q
Good-Bye
>>>
'''
