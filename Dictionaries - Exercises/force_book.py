force_side_and_users_dict = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        user_is_part_of_the_force = False
        for value in force_side_and_users_dict.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_and_users_dict.keys():
                force_side_and_users_dict[force_side] = [force_user]
            else:
                force_side_and_users_dict[force_side].append(force_user)
    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        for key, value in force_side_and_users_dict.items():
            if force_user in value:
                force_side_and_users_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_and_users_dict.keys():
            force_side_and_users_dict[force_side] = [force_user]
        else:
            force_side_and_users_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_sides, force_users in force_side_and_users_dict.items():
    if len(force_users) > 0:
        print(f"Side: {force_sides}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")
