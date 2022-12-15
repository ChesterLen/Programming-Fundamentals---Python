string = input()
explosion = 0
new_string = ""
for char in range(len(string)):
    if explosion > 0 and string[char] != ">":
        explosion -= 1
    elif string[char] == ">":
        new_string += string[char]
        explosion += int(string[char + 1])
    else:
        new_string += string[char]
print(new_string)
