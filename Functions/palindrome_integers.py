numbers = input().split(", ")


def palindrome(num):
    for i in num:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


palindrome(numbers)
