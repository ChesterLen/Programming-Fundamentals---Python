string = input()
split_string = string.split()
list1 = []
for char in split_string:
    integer = int(char)
    if integer > 0:
        integer = "-" + str(integer)
        integer = int(integer)
        list1.append(integer)
    elif integer < 0:
        list1.append(abs(integer))
    elif integer == 0:
        list1.append(integer)
print(list1)
