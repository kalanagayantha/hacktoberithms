"""
Challenge: Write a function that takes a list of two numbers
and return the sum of those two numbers plus the sum of all
the numbers between them.
"""

import random

lst_1 = [random.randint(0,9) for i in range(2)]  #importing random genarated numbers to a list call lst_1

def sum_all(lst_1):  #define the sum_all function 
    sum_nums = 0
    lst.sort()
    
    for num in range(lst_1[0], lst_1[1]+1):
            sum_nums += num

    print(lst_1) 
    return sum_nums
