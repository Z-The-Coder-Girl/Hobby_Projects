import random


def reverse_table(table):
    """
    :param: table (type list):
    :return: table (type list )where each row has been reversed
    """
    new_table = [x[::-1] for x in table]
    return new_table


def transpose_table(table):
    """
    :param: table( type list):
    :return: transpose of the given table ( which is a list)
    """
    new_table = [[table[j][i] for j in range(len(table))] for i in range(len(table[0]))]
    return new_table


def choose_random_square(table):
    """
    choosing a random empty square in the given table for inserting a new random value(if required)
    :param: table(type list) :
    :return: ( either None if there is no empty place or (x,y) as a tuple which shows  coordination of  selected  place
    """
    empty_squares_list = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            if not table[i][j].value:
                empty_squares_list.append((i, j))

    if empty_squares_list == []:
        return None
    else:
        rndm_sqr = random.randint(0, len(empty_squares_list)-1)
        return empty_squares_list[rndm_sqr]


def cleanup_table(table):
    """
    :param: table(type list):
    :return: cleaned table(list) where the  some internal states variables are all back to default for next move
    """
    for row in table:
        for square in row:
            square.original_value = True
    return table
