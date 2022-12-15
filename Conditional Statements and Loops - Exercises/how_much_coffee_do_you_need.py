command = input()
coffees_count = 0
while command != "END":
    event = command
    if event == "coding".upper():
        coffees_count += 2
    elif event == "coding".lower():
        coffees_count += 1
    if event == "cat".upper():
        coffees_count += 2
    elif event == "cat".lower():
        coffees_count += 1
    if event == "dog".upper():
        coffees_count += 2
    elif event == "dog".lower():
        coffees_count += 1
    if event == "movie".upper():
        coffees_count += 2
    elif event == "movie".lower():
        coffees_count += 1
    command = input()
if coffees_count > 5:
    print("You need extra sleep")
else:
    print(coffees_count)
