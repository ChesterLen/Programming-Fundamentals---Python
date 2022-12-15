phonebook_dict = {}
while True:
    command = input()
    if "-" not in command:
        break
    name, phone = command.split("-")
    phonebook_dict[name] = phone
for check in range(int(command)):
    name = input()
    if name in phonebook_dict.keys():
        print(f"{name} -> {phonebook_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")
