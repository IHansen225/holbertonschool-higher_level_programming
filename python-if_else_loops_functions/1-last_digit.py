#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = int(repr(number)[-1]) if number > 0 else (int(repr(number)[-1])) * -1
if ld == 0:
    extra = " and is 0"
elif ld != 0 and ld < 6:
    extra = " and is less than 6 and not 0"
elif ld > 5:
    extra = " and is greater than 5"
else:
    extra = ""
print(f"Last digit of {number} is {ld}{extra}")
