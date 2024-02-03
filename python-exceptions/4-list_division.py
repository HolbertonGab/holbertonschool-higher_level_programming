#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
        except IndexError:
            print("out of range")
            value_1 = 0

        try:
            value_2 = my_list_2[i]
        except IndexError:
            print("out of range")
            value_2 = 0

        if not (isinstance(value_1, (int, float)) and isinstance(value_2, (int, float))):
            print("wrong type")
            result.append(0)
        elif value_2 == 0:
            print("division by 0")
            result.append(0)
        else:
            result.append(value_1 / value_2)

    return result
