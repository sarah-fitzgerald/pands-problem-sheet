#This program calculates BMI from users inputs
#Author: Sarah Fitzgerald

#Inputs for height (cm) and weight (kg) from user
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))

#Maths conversion - cm to m²
metresquared = (height/100) ** 2

#Calculation of users BMI
BMI = round (weight / metresquared, 2)

#Outputs users BMI 
print ("BMI is {}".format(BMI))