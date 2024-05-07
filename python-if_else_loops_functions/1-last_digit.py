#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "is"
lastdigit = abs(number) % 10
str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"
if lastdigit > 5:
     print(f"Last digit of {number} {str} {lastdigit} {str1}")
elif lastdigit == 0:
     print(f"Last digit of {number} {str} {lastdigit} {str2}")
elif lastdigit < 6 and lastdigit != 0:
     print(f"Last digit of {number} {str} {lastdigit} {str3}")