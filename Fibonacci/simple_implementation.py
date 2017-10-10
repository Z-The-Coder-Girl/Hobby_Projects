def fibonacci_sum(element_number):
    """
    :param element_number: int : element number can be 0,1,2,3,4,...
    :return:(int) sum of fibonacci sequence up to  inserted index
    """
    fib_sum = 1
    prev_1 = 1  # last element value in sequence
    prev_2 = 0  # second last element value in sequence

    if element_number == 0 or element_number == 1:
        fib_sum = element_number
        return fib_sum

    for cntr in range(2, element_number):
        new_fib = prev_1 + prev_2
        fib_sum += new_fib
        prev_2 = prev_1
        prev_1 = new_fib
    return fib_sum






