num = input().split(".")
string = ""
for i in num:
    string += i
for i in range(len(string)):
    if string[i] == 0:
        int(string) + 1
next_version = int(string) + 1
string_next_version = str(next_version)
print(f"{str(string_next_version[0])}.{str(string_next_version[1])}.{str(string_next_version[2])}")
