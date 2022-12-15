gifts = input().split(" ")
command = input()
while not command == "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for gift in range(len(gifts)):
            if command[1] in gifts[gift]:
                gifts[gift] = "None"
    elif "Required" in command:
        for gift in range(len(gifts)):
            if gift == int(command[2]):
                gifts[gift] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[1]
    command = input()
while "None" in gifts:
    gifts.remove("None")
for gift in gifts:
    print(gift, end=" ")
