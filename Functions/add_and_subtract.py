number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def add_and_subtract(a, b, c):
    result = a + b
    result -= c
    return result


print(add_and_subtract(number_1, number_2, number_3))
