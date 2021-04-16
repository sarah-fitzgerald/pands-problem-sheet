#Takes a positive floating-point number as an input and outputs an approximation of its squareroot
#Author: Sarah Fitzgerald

def newton_method (number, number_iters = 500):
    a = float(number) #This is the number to get the square root of

    for i in range (number_iters) :
        number = 0.5 * (number + a /number) # x_(n+1) = 0.5 * (x_n +a / x_n) forumla to run Newton Method: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

    return number

x = float(input("Please enter a positive number: ")) # Request user to input a positive number

y = (newton_method(x)) #Once a positive number is inputted, the squareroot is found using the Newton Method

print (round(y, 1)) # Round the number to one decimal place to match the example provided: https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place