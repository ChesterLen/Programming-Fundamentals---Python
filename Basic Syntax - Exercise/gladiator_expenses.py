lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
broken_shield_count = 0
for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        total_price += helmet_price
    if fight % 3 == 0:
        total_price += sword_price
        if fight % 2 == 0:
            total_price += shield_price
            broken_shield_count += 1
            if broken_shield_count % 2 == 0:
                total_price += armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
