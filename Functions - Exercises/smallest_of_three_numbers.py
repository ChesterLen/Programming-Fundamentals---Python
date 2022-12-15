number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def smallest_of_three(a, b, c):
    list1 = [a, b, c]
    return min(list1)


print(smallest_of_three(number_1, number_2, number_3))
