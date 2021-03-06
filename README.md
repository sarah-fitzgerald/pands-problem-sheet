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




  <ol>
    
  </ol>




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

User is prompted to inter height and weight as an float. After input, weight is divided by height in meters to the power of 2. After which the output it printed.

### Reference

1. stackoverflow: https://stackoverflow.com/questions/27864750/bmi-calculator-always-return-0-python

<!-- Task 2 -->
## Task 2 secondstring.py

Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

### Code

    sentence = str(input( "Please enter a sentence: " )) [::-1] 
    print (sentence[::2])

### Explanation of code

User is prompted to input a string, then [::-1] reverses the string.. [::2] prints our every second letter.

### Reference
1. W3Schools: https://www.w3schools.com/python/python_howto_reverse_string.asp
2. stackoverflow: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220

<!-- Task 3 -->
## Task 3 collatz.py

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

### Code
        x = int(input("Please enter a positive number: ")) 

        def collatz(x): 
         if x % 2 == 0: 
                return x // 2 
           
            else: 
                return x * 3 + 1

        while x != 1: 

            print (x)
            x = collatz(int(x))

### Explanation of code
Asks user to input a positive integer, here (x) is defined as a integer. Then the progeram checks if the number (x) is greater than 0. Next within the collatz function, if the remainder number is divided by 2 is 0 then it is even and it is returned to the function or else if the  number divided by 2 is not 0 then it is odd and the returned result is * 3 + 1 and returned to the function. 

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
Imported the date object in python, then used the date.weekday() object to return the day of the week as an interger, in this case Monday is 0, Tuesday is 1, Wednesday is 2, Thursday is 3, Friday is 4, Saturday is 5, Sunday is 6. If the integer return is between 0-4 then it will print "Yes, unfortunately today is a weekday," but if it returns 5 or 6 it will print "It is the weekend, yay!"

### References
1. Python.org: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
2. https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

<!-- Task 5 -->
## Task 5 squareroot.py
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

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
The Newton Method is applied to an inputted positive number, after which a set of iteration is run to find the approminate squareroot. The outputted number is rounded to 1 decimal place to match the example given in the exercise.

### References
1. https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
2. https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place
3. https://www.youtube.com/watch?v=2GrfaB88w4M 
4. https://en.wikipedia.org/wiki/Newton%27s_method

<!-- Task 6 -->
## Task 6 es.py moby-dick-txt
Write a program that reads in a text file and outputs the number of e's it contains.

The program should take the filename from an argument on the command line.

### Code
        def letterFrequency(filename, letter): 

            file = open(filename, "r") 

            text = file.read() 

            return text.count(letter) letters

        filename = str(input("Please choose a file: ")) 

        print (letterFrequency(filename, "e")) 

### Explanation of code
Created a function to return the letter count. After this, it will open the file in read mode and then the content of the file is stored as a varible. Next, used the count() method to count the number of letters. Then user is asked to input the name of the file as a string with which they would like to count the number of e's in it. Finally, the number of e's contained in the text is printed.

### References
1. https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
2. https://www.w3schools.com/python/ref_list_count.asp 
3. https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python

<!-- Task 7 -->
## Task 7 plottask.py
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

### Code
        import matplotlib.pyplot as plt
        mport numpy as np

        x = np.arange(0.0, 4.0) 

        x = x #This is f(x)
        y = x ** 2 #This is g(x)
        z = x ** 3 #This is h(x)

        plt.plot (x, linestyle = 'dashed', label = 'f(x)', color ='r') 
        plt.plot (y, linestyle = 'dashed', label = 'g(x)', color = 'b') 
        plt.plot (z, linestyle = 'dashed', label = 'h(x)', color = 'g')

        plt.xlim(0.0, 3.5) 
        plt.ylim(0.0, 30.0) 

        plt.xlabel ('X-Axis') 
        plt.ylabel ('Y-Axis') 

        plt.title('f(x)=x, g(x)=x2 and h(x)=x3') 

        plt.legend() 
        plt.show()

![Graph](https://github.com/sarah-fitzgerald/pands-problem-sheet/blob/3e08b7eb73ed0dae9c099ac00c7668c231936cff/plottask.py.png)

### Explanation of code
Imported numpy as "np" and matplotlib.pyplot as "plt." Then defined the x-axis valuesand the range was from 0.0 to 4.0. Next defined the y-axis values as x,y,z. Then plotted the values using plt.plot. Formatted each point by linestyle, label, and colour. Then set limits for the x-axis and y-axis that appear on the graph and added a title to the graph. Finally the graph can be represented

### References
1. https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
2. https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm
3. https://matplotlib.org/stable/tutorials/introductory/pyplot.html
4. https://stackoverflow.com/questions/17941083/how-to-label-a-line-in-matplotlib-python/17942066
5. https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

## Template for README

https://github.com/othneildrew/Best-README-Template.git