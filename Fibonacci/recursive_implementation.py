def fibonacci_value(element_number, fib_dict={}):
    """

    :param:element_number(non negative integer ) where we want to see the fibonacci value of that index
    :param fib_dict: ( optinal) current dictionary of fibonacci if any of it has been built during previous steps
    :return: the calculated value for required index( integer
    """
    if element_number == 0 or element_number == 1:
        fib_dict[element_number] = element_number
        return element_number
    elif element_number in fib_dict:
        return fib_dict[element_number]
    else:
        fib_dict[element_number] = fibonacci_value(element_number-1, fib_dict) + fibonacci_value(element_number-2, fib_dict)
        return fib_dict[element_number]

