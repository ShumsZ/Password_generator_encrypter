# without user input
import random

variables = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890","£$%&!*"]

result = '' # need to define result variable to store the value of result in for each iteration of the loop
for i in range(3):

    for element in variables:
        result += str(random.choice(element)) 
        

print(result)
