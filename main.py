# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#importing modules
from math import *

from Solver.input import *
from Solver.parseExcercises import *
from Solver.solve import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    saved_excercises = input()
    parseExcercises(saved_excercises)
    # print(saved_excercises)
    solve(saved_excercises)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
