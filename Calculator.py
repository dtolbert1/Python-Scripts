# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:39:43 2016

@author: DAndre
"""

print('Welcome to the Calculator')
number1 = int(input('What is your first number?  '))
operation = input('Which operation would you like to perform? +, -, *, or /   ')
number2 = int(input('What is your second number?  '))

if operation == '+':
    answer = number1 + number2

elif operation == '-':
    answer = number1 - number2
    
elif operation == '*':
    answer = number1 * number2
    
elif operation == '/':
    answer = number1 / number2
    
print('The answer is ' + str(answer))