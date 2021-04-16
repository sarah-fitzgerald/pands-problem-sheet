#This program takes user string inputs and outputs every second letter in reverse order
#Sentence for weekly task: The quick brown fox jumps over the lazy dog.
#Author: Sarah Fitzgerald

#Asks user to input a sentence as a string
sentence = str(input( "Please enter a sentence: " )) [::-1] #[::-1] reverses the sentence - https://www.w3schools.com/python/python_howto_reverse_string.asp

#Prints out every second letter of the sentence in reverse order
print (sentence[::2]) #[::2] prints our every second letter - https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220