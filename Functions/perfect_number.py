number = int(input())


def perfect_number(num):
    sum1 = 0
    for i in range(1, num):
        if num % i == 0:
            sum1 += i
    if sum1 == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(number))
