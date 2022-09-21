quantity_decoration = int(input())
days_until_christmas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
points_spirit_per_shopping_day = 0
total_price = 0
for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_decoration += 2
    if day % 2 == 0:
        points_spirit_per_shopping_day += 5
        total_price += ornament_set * quantity_decoration
    if day % 3 == 0:
        points_spirit_per_shopping_day += 3 + 10
        total_price += (tree_skirt + tree_garland) * quantity_decoration
    if day % 5 == 0:
        points_spirit_per_shopping_day += 17
        total_price += tree_lights * quantity_decoration
        if day % 3 == 0:
            points_spirit_per_shopping_day += 30
    if day % 10 == 0:
        points_spirit_per_shopping_day -= 20
        total_price += tree_lights + tree_skirt + tree_garland
if days_until_christmas % 10 == 0:
    points_spirit_per_shopping_day -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {points_spirit_per_shopping_day}")
