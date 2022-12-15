from collections import Counter
my_dict = {}
command = input()
language_list = []
while command != "exam finished":
    command = command.split("-")
    username = command[0]
    language = command[1]
    if len(command) > 2:
        points = int(command[2])
    if username not in my_dict.keys():
        my_dict[username] = []
        my_dict[username].append(language)
    my_dict[username].append(points)
    if language == "banned":
        del my_dict[username]
    else:
        language_list.append(language)
    for value in my_dict.values():
        max_num = 0
        for i in value[1::]:
            if max_num < i:
                max_num = i
                value.append(max_num)
                value.pop(value.index(i))
        for i in value[1::]:
            if i < max_num:
                value.pop(value.index(i))
    command = input()
print("Results:")
for name, points in my_dict.items():
    print(f"{name} | {points[1]}")
submissions = Counter(language_list)
print("Submissions:")
for item, value in submissions.items():
    print(f"{item} - {value}")
