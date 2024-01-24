#!/usr/bin/env python3
def uppercase(str):
    for index in str:
        if "a" <= index <= "z":
            upper_char = chr(ord(index) - 32)
        else:
            upper_char = index
        print("{}".format(upper_char), end="")
    print("\n")
