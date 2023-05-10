#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(r"{number} is positive")
elif number == 0:
    print(r"{number} is zero")
else:
    print(r"{number} is negative")
