# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 9/10/2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here 

# TO DO 2: define the function with name `is_even`.

# TO DO 3: Call the function `is_even`.
def is_even(mylist):
    for number in mylist:
        if number % 2==0:
            return True
        else:
            return False
print(mylist)
