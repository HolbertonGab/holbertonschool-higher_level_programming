#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
print("Last digit of", number, "is", end=" ")
if int(number_str[-1]) > 5:
    print(number_str[-1], "and is greater than 5")
elif int(number_str[-1]) < 6 and int(number_str[-1]) != 0:
    print(number_str[-1], "and is less than 6 and not 0")
else:
    print(number_str[-1], "and is 0")
