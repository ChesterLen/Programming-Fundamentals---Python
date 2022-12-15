command = input()
while command != "Welcome!":
    student_name = command
    if student_name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif len(student_name) > 6:
        print(f"{student_name} goes to Hufflepuff.")
    command = input()
else:
    print("Welcome to Hogwarts.")
