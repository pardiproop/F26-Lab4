# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 9/10/2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.
def sum(num1, num2):
    return num1+num2
def main():
    num1=int(input("Enter a Number: "))
    num2=int(input("Enter Another Number: "))
    result=sum(num1, num2)
    print("The Result:", result)
if __name__ == "__main__":
    main()
