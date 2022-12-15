command = input()
while command != "End":
    string = command
    if string != "SoftUni":
        for letter in string:
            print(letter * 2, end="")
        print()
    command = input()
