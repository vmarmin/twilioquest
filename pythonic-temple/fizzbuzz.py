#!/usr/bin/env python3

# Create a program that accepts any number of command line arguments.
# The arguments will be whole/integer numbers. Your script will need to examine all
# these numbers and execute the following conditional logic:

# If the number is divisible by 3, print the text: fizz
# If the number is divisible by 5, print the text: buzz
# If the number is divisible by both 3 and 5, print the text: fizzbuzz
# If none of the above are true, print the number

import sys

num_list = [int(i) for i in sys.argv[1:]]
for num in num_list:
    divBy3 = num % 3 == 0
    divBy5 = num % 5 == 0
    if divBy3 and divBy5:
        print("fizzbuzz")
    elif divBy3:
        print("fizz")
    elif divBy5:
        print("buzz")
    else:
        print(num)
