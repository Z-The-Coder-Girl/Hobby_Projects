"""
User need to run fibonacci.py
 This code get inputs from user ( index for fobonacci sequence starting 0, so first element is at index '0' not '1')
based on that the code will return:
    1) value of  entered Fibonacci element and
    2)(optional) sum of the sequence up to that element
 The idea is to show both recursive and  a non-recursive implementation in this code,
but the code could also be written only with one implementation eaily

Author: Zohreh Abdeyazdan
OCT 2017
"""

import logging
from recursive_implementation import fibonacci_value
from simple_implementation import fibonacci_sum
logging.basicConfig(level=logging.INFO)


EXPECTED_FUNC_VALUE = {1: 'SEQUENCE', 2: 'SUM'}  # valid inputs for desired functionality
fib_value = None  # initialization for the sequence
fib_sum = None  # initialization for sum of sequence


last_element = raw_input("Please enter the element number of Fibonacci sequence you wish to see its value\n"
                         "(element numbers are starting from 0)\n")
# evaluate if user input is a meaningful element number
try:
    last_element = int(last_element)
    if last_element < 0:
        raise ValueError

except ValueError:
    logging.error("WRONG INPUT!!! please enter a non-negative integer for element number\n")
    raise ValueError()


desired_func = raw_input("Press '1', If you only wish to see value of your entered element\n"
                         "Press '2', If you  also wish to see the sum of the sequence up to your element\n")

# check if user enters an expected value for functionality
try:
    desired_func = int(desired_func)
    if desired_func not in EXPECTED_FUNC_VALUE:
        raise ValueError
except ValueError:
    logging.error("WRONG INPUT!!! please enter a valid input for  the functionality you want to be done\n")
    raise ValueError()


if EXPECTED_FUNC_VALUE[desired_func] == "SUM":
    fib_sum = fibonacci_sum(last_element)  # non-recursive solution
    logging.info("Sum of Fibonacci sequence up to {}th element is: {}\n".format(last_element, fib_sum))


fib_value = fibonacci_value(last_element)  # recursive solution
logging.info("value of {}th element of Fibonacci sequence is: {}\n".format(last_element, fib_value))