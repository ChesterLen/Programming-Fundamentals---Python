strings = input().split()
string_1 = strings[0]
string_2 = strings[1]
total_chars_code = 0
if len(string_1) > len(string_2):
    for char in range(len(string_2)):
        total_chars_code += ord(string_1[char]) * ord(string_2[char])
    for char in range(len(string_2), len(string_1)):
        total_chars_code += ord(string_1[char])
elif len(string_2) > len(string_1):
    for char in range(len(string_1)):
        total_chars_code += ord(string_2[char]) * ord(string_1[char])
    for char in range(len(string_1), len(string_2)):
        total_chars_code += ord(string_2[char])
elif len(string_1) == len(string_2):
    for char in range(len(string_1)):
        total_chars_code += ord(string_1[char]) * ord(string_2[char])
print(total_chars_code)
