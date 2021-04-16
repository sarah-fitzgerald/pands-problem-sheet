#This program asks user to input any positive integer
#Then outputs the successive values
#Author: Sarah Fitzgerald

#https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php

x = int(input("Please enter a positive number: ")) # Asks user to input a positive number

def collatz(x): #Defines the funcition and the number is the parameter
    if x % 2 == 0: #If the remainder number is divided by 2 is 0 then it is even
        return x // 2 #This returns the result to the function
           
    else: #If the remainder number divided by 2 is not 0 then it is odd
        return x * 3 + 1

while x != 1: #Loop to print until the number is 1

    print (x)
    x = collatz(int(x)) #The collatz function passes the number until it gets to 1: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff