#This program asks user to input any positive integer
#Then outputs the successive values
#Author: Sarah Fitzgerald

#https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php

number = int(input("Please enter a positve integer: "))

x = []
x.append(number)

while (number > 1) and (number != 0):

    if (number % 2 == 1):
        number = number // 2

    elif (number % 2 == 1):
        number = 3 * number + 1

print (x)


