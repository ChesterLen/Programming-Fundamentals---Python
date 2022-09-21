footballer_name = input()
best_footballer_name = ""
current_footballer_name = ""
score = 0
while footballer_name != "END":
    goal = int(input())
    current_footballer_name = footballer_name

    if goal > score:
        score = goal
        best_footballer_name = footballer_name

    if goal >= 10:
        break

    footballer_name = input()

print(f"{best_footballer_name} is the best player!")

if score >= 3:
    print(f'He has scored {score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {score} goals.')
