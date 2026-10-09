# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 9/10/2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.
def compute(num1, num2, operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    else operation=="/":
        return num1/num2

compute(13,45,'*')
compute(13,45,'/')
compute(13,45,'-')
compute(13,45,'+')
compute(13,45)  # since only two parameters are passed the default value of symbol should be used.
