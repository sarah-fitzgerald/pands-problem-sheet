<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->


<!-- Header -->
<br />
<p align="center">

  <h3 align="center">pands-problem-sheet - Sarah Fitzgerald - G00398363</h3>

This README explains the code used to solve weekly tasks assigned from the Programming and Scripting module for the postgraduate diploma in Computer Science with Data Analytics at GMIT
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#Task 1 bmi.py">Task 1 bmi.py</a></li>
    <li><a href="#Task 2 secondstring.py">Task 2 secondstring.py</a></li>
    <li><a href="#Task 3 collatz.py">Task 3 collatz.py</a></li>
    <li><a href="#Task 4 weekday.py">Task 4 weekday.py</a></li>
    <li><a href="#Task 5 squareroot.py">Task 5 squareroot.py</a></li>
    <li><a href="#Task 6 es.py moby-dick-txt">Task 6 es.py moby-dick-txt</a></li>
    <li><a href="#Task 7 plottask.py">Task 7 plotttask</a></li>
    <li><a href="#Task 8">Task 8</a></li>
  </ol>
</details>



<!-- Task 1 -->
## Task 1 bmi.py

Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared:

## Code

    height = float(input("Enter height (cm): "))
    weight = float(input("Enter *weight (kg): "))

    metresquared = (height/100) ** 2
    BMI = round (weight / metresquared, 2)

    print ("BMI is {}".format(BMI))


### Explanation of code

User is prompted to inter height and weight as an float. After input, weight is divided by height in meters to the power of 2 [REF 1.]. After which the output it printed.

### Reference

1. stackoverflow: https://stackoverflow.com/questions/27864750/bmi-calculator-always-return-0-python

<!-- Task 2 -->
## Task 2 secondstring.py

Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

### Code

    sentence = str(input( "Please enter a sentence: " )) [::-1] 
    print (sentence[::2])

### Explanation of code

User is prompted to input a string, then [::-1] reverses the string [REF 1.]. [::2] prints our every second letter [REF 2.]

### Reference
1. W3Schools: https://www.w3schools.com/python/python_howto_reverse_string.asp
2. stackoverflow: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220

<!-- Task 3 -->
## Task 3 collatz.py

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

### Code
    number = int(input("Please enter a positve integer: "))

    x = []
    x.append(number)

    while (number > 1) and (number != 0):

        if (number % 2 == 1):
            number = number // 2

        elif (number % 2 == 1):
            number = 3 * number + 1

    print (x)

### Explanation of code

### References
1. W3Schools: https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php


<!-- Task 4 -->
## Task 4 weekday.py

Write a program that outputs whether or not today is a weekday.

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

### Code

    import datetime

    day = datetime.datetime.today().weekday()

        if day < 5:
         print ("Yes, unfortunately today is a weekday")

        else:
         print ("It is the weekend, yay!")

    print (day)

### Explanation of code
Imported the date object in python [REF 1.], then used the date.weekday() object to return the day of the week as an interger, in this case Monday is 0, Tuesday is 1, Wednesday is 2, Thursday is 3, Friday is 4, Saturday is 5, Sunday is 6 [REF 2.]. If the integer return is between 0-4 then it will print "Yes, unfortunately today is a weekday," but if it returns 5 or 6 it will print "It is the weekend, yay!"

### References
1. Python.org: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
2. https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

<!-- Task 5 -->
## Task 5 squareroot.py

### Code
    def newton_method (number, number_iters = 500):
        a = float(number) 

       for i in range (number_iters) :
            number = 0.5 * (number + a /number) 

        return number

    x = float(input("Please enter a positive number: ")) 

    y = (newton_method(x)) 

    print (round(y, 1)) 

### Explanation of code
Based code off of [Ref.1], the Newton Method is applied to an inputted positive number. After which a set of iteration is run to find the approminate squareroot. The outputted number is rounded to 1 decimal place to match the example given in the exercise [Ref. 2]

### References
1. https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
2. https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place
3. https://www.youtube.com/watch?v=2GrfaB88w4M 
4. https://en.wikipedia.org/wiki/Newton%27s_method

<!-- Task 6 -->
## Task 6 es.py moby-dick-txt

### Code

### Explanation of code

### References

<!-- Task 7 -->
## Task 7 plottask.py

### Code

### Explanation of code

### References

## Template for README

https://github.com/othneildrew/Best-README-Template.git