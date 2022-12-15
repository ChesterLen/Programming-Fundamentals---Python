orders_count = int(input())
final_price = 0
for order in range(1, orders_count + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    total_price = days * capsules_needed_per_day * capsule_price
    final_price += total_price
    print(f"The price for the coffee is: ${total_price:.2f}")
print(f"Total: ${final_price:.2f}")
