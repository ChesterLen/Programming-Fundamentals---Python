pet_food = int(input())
pet_food_in_grams = pet_food * 1000
command = input()
total_food_eaten = 0
while command != "Adopted":
    food_eaten = int(command)
    total_food_eaten += food_eaten
    command = input()
food_left = abs(total_food_eaten - pet_food_in_grams)
if total_food_eaten <= pet_food_in_grams:
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    print(f"Food is not enough. You need {food_left} grams more.")
