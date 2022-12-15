string = input()
for i in string:
    while i * 2 in string:
        string = string.replace(i * 2, i)
print(string)
