numbers = input().split(", ")
list_ints = [int(x) for x in numbers]
group_2 = 0
group = 10
len_list_int = len(list_ints)
while len_list_int > 0:
    filtered_list = list(filter(lambda x: group_2 < x <= group, list_ints))
    print(f"Group of {group}'s: {filtered_list}")
    for i in filtered_list:
        if i in list_ints:
            list_ints.remove(i)
    group += 10
    group_2 += 10
    if len(list_ints) == 0:
        break
