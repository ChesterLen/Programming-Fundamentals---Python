numbers_count = int(input())
for num in range(1, numbers_count + 1):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
