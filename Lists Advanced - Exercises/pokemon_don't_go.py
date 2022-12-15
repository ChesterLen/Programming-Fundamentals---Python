list1 = [int(x) for x in input().split(" ")]
sum_removed = 0
while len(list1) != 0:
    pokemon = int(input())
    removed = 0
    if 0 <= pokemon < len(list1):
        removed = list1.pop(pokemon)
    elif 0 > pokemon:
        removed = list1[0]
        list1[0] = list1[-1]
    else:
        removed = list1[-1]
        list1[-1] = list1[0]
    sum_removed += removed
    for i in range(len(list1)):
        if list1[i] <= removed:
            list1[i] += removed
        else:
            list1[i] -= removed
print(sum_removed)
