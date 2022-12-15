string = input().split()
joined_string = "".join(string)
my_dict = {}
for char in joined_string:
    my_dict[char] = joined_string.count(char)
for key, value in my_dict.items():
    print(f"{key} -> {value}")
