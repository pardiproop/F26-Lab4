# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 9/10/2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.
numbers=(range(2, 11))
numbers=map(lambda x: x * 2, [1, 2, 3], numbers)  # Output: [2, 4, 6]
print(numbers)
divisible_by_2=filter(lambda x: x > 2, [1, 2, 3, 4], numbers)  # Output: [3, 4]
print(divisible_by_2)
