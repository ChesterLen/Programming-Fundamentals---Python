numbers = input().split(" ")
count_of_numbers_to_remove = int(input())
list1 = []
list1_as_string = 0
for num in numbers:
    list1.append(int(num))
for number in range(count_of_numbers_to_remove):
    list1.remove(min(list1))
print(*list1, sep=", ")
