list1 = input().split(", ")
list2 = input().split(", ")
list3 = []
for i in list1:
    for j in list2:
        if i in j:
            list3.append(i)
            for k in list3:
                if list3.count(k) > 1:
                    list3.remove(k)
print(list3)
