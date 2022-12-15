number = int(input())


def loading_bar(num):
    percent_sign_count = (num // 10) * "%"
    dots_count = (10 - (num // 10)) * "."
    if num < 100:
        return f"{num}% [{percent_sign_count + dots_count}]\nStill loading..."
    elif num == 100:
        return f"{num}% Complete!\n[{percent_sign_count + dots_count}]"


print(loading_bar(number))
