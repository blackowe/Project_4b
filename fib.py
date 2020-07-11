# Author: Erik Blackowicz
# Date: 7/11/20
# Description: Project 4b - Fibonacci sequence

def fib(input):
    ''' Takes positive integer from user and returns the number at that position
    in the Fibonacci sequence.'''
    num1 = 0  # 1st value in Fib. sequence
    num2 = 1 # 2nd value in Fib. sequence
    for i in range(0, input):
        x = num1 # x acts as a temporary holder
        num1 = num2  # reassign of num2 value to num1
        num2 = x + num2 # assigns num2 as the sum of preceding 2 values
    return num1

