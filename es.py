#Program that reads in a text files name and outputs the number of e's it contains
#Author: Sarah Fitzgerald

def letterFrequency(filename, letter): #Funcition to return the letter count: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

    file = open(filename, "r") #r will read the opened file

    text = file.read() #Stores the content of the file in a variable

    return text.count(letter) #Uses count() to count the number of letters

filename = str(input("Please choose a file: ")) #Requests user input the file location on their PC

print (letterFrequency(filename, "e")) #Prints out the amount of e's in the chosen text