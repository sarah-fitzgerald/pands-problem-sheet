pands-problem-sheet
Sarah Fitzgerald - 

Introduction:
This README explains the code used to solve weekly tasks assigned from the Programming and Scriptin module for the postgraduate diploma in Computer Science with Data Analytics at GMIT

Task 1:
Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
    The inputs are the person's height in centimetres and weight in kilograms.
    The output  is their weight divided by their height in metres squared.

Code:
    height = float(input("Enter height (cm): "))
    weight = float(input("Enter weight (kg): "))

    metresquared = (height/100) ** 2
    BMI = round (weight / metresquared, 2)

    print ("BMI is {}".format(BMI))

Explanation of code:
User is prompted to inter height and weight as an float. After input, weight is divided by height in meters to the power of 2 [REF 1.]. After which the output it printed. 

Reference:
1. stackoverflow: https://stackoverflow.com/questions/27864750/bmi-calculator-always-return-0-python

Task 2:
Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

Code:
    sentence = str(input( "Please enter a sentence: " )) [::-1] 
    print (sentence[::2]) 

Explanation of code:
User is prompted to input a string, then [::-1] reverses the string [REF 1.]. [::2] prints our every second letter [REF 2.]

Reference:
1. W3Schools: https://www.w3schools.com/python/python_howto_reverse_string.asp
2. stackoverflow: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220

Task 3:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Code:
