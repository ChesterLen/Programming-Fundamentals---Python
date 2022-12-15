parking_dict = {}
commands_count = int(input())
for _command in range(commands_count):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in parking_dict.keys():
            print(f"ERROR: already registered with plate number {parking_dict[username]}")
        elif username not in parking_dict.keys():
            parking_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_dict[username]
for username, license_plate_number in parking_dict.items():
    print(f"{username} => {license_plate_number}")
