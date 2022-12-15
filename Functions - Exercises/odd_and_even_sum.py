number = int(input())


def sum_odd_and_even(num):
    odd_sum = 0
    even_sum = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 != 0:
            odd_sum += int(i)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(sum_odd_and_even(number))
