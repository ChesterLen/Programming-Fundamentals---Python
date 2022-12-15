strings_count = int(input())
for string in range(1, strings_count + 1):
    string_example = input()
    if "_" in string_example or "," in string_example or "." in string_example:
        print(f"{string_example} is not pure!")
    else:
        print(f"{string_example} is pure.")
