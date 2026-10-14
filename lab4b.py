# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 9/10/2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here
def even_numbers(mylist):

# TO DO 2: Create the function.
    newlist=[]
    for number in mylist:
        if number%2==0:
            newlist.append(number)
    return newlist

# TO DO 3: Call the function.
mylist=[2, 1, 6, 5, 3, 4, 8, 9]
result=even_numbers(mylist)
print(result)
