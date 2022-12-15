string = input()
for char in range(len(string)):
    if string[char] == ":":
        print(f":{string[char + 1]}")
