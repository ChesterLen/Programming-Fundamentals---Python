numbers = input().split(" ")
list1 = []
for i in numbers:
    list1.append(int(i))
print(f"The minimum number is {min(list1)}")
print(f"The maximum number is {max(list1)}")
print(f"The sum number is: {sum(list1)}")
