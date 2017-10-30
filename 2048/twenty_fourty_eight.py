"""
User  need to run ten_twenty_four.py
This is a simplified version of 2048 game( the famous app), this one only interact with user through console.
Each time it just prints the current table and ask user for the next input( movement )
User choose to move squares to Left. Right, Up and Down just like the original 2048
If user enter an unexpected value ( other than U, D, R, L either upper or lower case),
the game with be over  with printing a proper message

 It is a 4 by 4 table ( can be extended to other sizes with little adjustment),
in the begging and also after each movement ( if that move causes any change),
a random empty spot is chosen and a random allowed value will be inserted.
Once no more movement is possible the game is over,
so the play continues as long as there is still possibility of movements.


Author : Zohreh Abdeyazdan
OCT 2017
"""

from pprint import pprint
import copy
from table_functions import *


class Square():
    """
    Square defines the object which can have valid s and None,
      and some other attributes to handle changes and follow states based on the game stategy
       each square with represent a spot in table
    """
    VALID_VALUES = (2, 4)  # values that are allowed to be randomly inserted in an empty square

    def __init__(self):
        self.value = None
        self.original_value = True

    def add_value(self, new_number):
        if not self.value:
            self.value = new_number
            return True
        elif self.value == new_number:
            self.value += new_number
            return True
        else:
            return False

    def set_random_value(self):
        if not self.value:
            self.value = random.choice(self.VALID_VALUES)

    def remove_value(self):
        self.value = None


class TwentyFortyEight(object):
    MATRIX_SIZE = 4  # class variable accessible Through class name directly and through instances (self.) as well
    start_num_sqrs = 2

    def __init__(self):
        """
        initializing a table(list of lists) and fill each element with an instance of Square Object
        we also start with inserting one random value in a random spot
        """
        self._table = []
        for row in range(0, self.MATRIX_SIZE):
            self._table.append([Square() for x in range(0, self.MATRIX_SIZE)])
        square_x = random.randint(0, self.MATRIX_SIZE-1)
        square_y = random.randint(0, self.MATRIX_SIZE-1)
        self._table[square_x][square_y].set_random_value()
        #print(self._table[square_x][square_y].value)
        self.keep_playing = True

    def print_table(self, table=None):
        """

        :param: table: ( type list) either print the given table or self._table by default in a table form for user
        :return: None
        """

        if not table:
            table = self._table
        for row in table:
            temp_row = [" " if x.value==None else x.value for x in row]
            pprint(temp_row)

    def equal_table(self, second_table):
        """
        to compare self._table with the second given table to see if values  of all objects in both tables are the same
        :param: second_table(type list)
        :return: True or False
        """

        for row_cntr in range(0, len(self._table)):
            for col_cntr in range(0, len(self._table[0])):
                if not self._table[row_cntr][col_cntr].value == second_table[row_cntr][col_cntr].value:
                    return False
        return True

    def play(self):
        """
        main method to keep running the game, terminating it and ask user for input when required
        this method taking care of rejecting wrong inputs,
         declare a game over and prepared parameter to call transit method
        :return: None
        """
        # next move Up, Down, Left, Right works with both upper case and lower case of the first letter
        valid_moves = ('U', 'D', 'L', 'R')

        while self.keep_playing:
            self.print_table()
            next_move = raw_input("Please enter your next move ({})\n".format(valid_moves)).upper()
            if next_move not in valid_moves:
                print('\n WRONG INPUT! choose your next move from valid-moves {}\n'.format(valid_moves))
                self.keep_playing = False
                continue
            else:
                # the idea is to deal with Left move based on original table
                # and call transit on the original table directly
                # for U, D, and R will reverse and/or tranpose the table
                #  and use the same transit function which is designed for L
                # once the transition is done,
                # we will turn the table to its original order by reversing the change(reverse,...)
                temp_table = copy.deepcopy(self._table)
                if next_move == 'L':
                    temp_table = self.transit(temp_table[:])

                elif next_move == 'R':
                    new_reverse_table = self.transit(reverse_table(temp_table[:]))
                    temp_table = reverse_table(new_reverse_table)
                else:
                    tr_table = transpose_table(temp_table) # transposed copy of  table
                    if next_move == 'U':
                        new_tr_table = self.transit(tr_table)
                        temp_table = transpose_table(new_tr_table)
                    else:
                        new_reverse_tr_table = self.transit(reverse_table(tr_table))
                        temp_table = transpose_table(reverse_table(new_reverse_tr_table))

            rand_empty_sqr = choose_random_square(temp_table)
            if not rand_empty_sqr:
                # no move is possible so game is over
                print("!!!Dude! No empty spot is left!!!! :D")
                self.keep_playing = False
                continue
            elif not self.equal_table(temp_table):
                # check if there has been any change after calling transit function
                # and insert a new random value in table if there was any change at all
                # if there is still an empty spot and there was a change,
                # so we insert a new random value in a random empty spot
                (i, j) = rand_empty_sqr
                temp_table[i][j].set_random_value()
            self._table = temp_table
            self._table = cleanup_table(self._table)

        print("\n________________GAME OVER_______________ :( \n")

    def transit(self, current_table):
        """
        we will take care of any movements and addition in  all spots and returning the new table to play method
        :param: current_table(type list) original table sent from play method after getting user input:
        :return: table(type list) after being done with the movements based on User Input
        """
        new_table = copy.deepcopy(current_table)
        for row in new_table:
            cntr = 0
            while cntr < len(row):
                if row[cntr].value is None:
                    cntr += 1
                    continue

                elif not cntr == 0:
                    if not row[cntr-1].value:
                        row[cntr-1].value = row[cntr].value
                        row[cntr].remove_value()
                        cntr -= 1
                        continue
                    elif row[cntr].value == row[cntr-1].value and row[cntr-1].original_value:
                        row[cntr-1].add_value(row[cntr].value)
                        row[cntr-1].original_value = False
                        row[cntr].remove_value()
                        cntr -= 1
                        continue

                if cntr < len(row)-1:
                    if row[cntr].value == row[cntr+1].value and row[cntr].original_value:
                        row[cntr].add_value(row[cntr+1].value)
                        row[cntr+1].remove_value()
                        row[cntr].original_value = False
                    cntr += 1
                else:
                    cntr += 1

        return new_table

if __name__ == "__main__":
    game = TwentyFortyEight()
    game.play()
