# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:54:17 2016

@author: DAndre
"""

for number in range(0,101):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)