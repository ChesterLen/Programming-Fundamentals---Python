factor = int(input())
count = int(input())
list1 = []
for num in range(1, count + 1):
    num *= factor
    list1.append(num)
print(list1)
