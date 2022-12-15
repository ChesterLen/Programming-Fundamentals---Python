budget = float(input())
price_1_kilo_flour = float(input())
price_eggs_pack = price_1_kilo_flour * 75 / 100
price_1l_milk = price_1_kilo_flour + (price_1_kilo_flour * 25 / 100)
colored_eggs_count = 0
breads_count = 0
one_bread_price = price_1_kilo_flour + price_eggs_pack + (price_1l_milk / 4)
while budget > one_bread_price:
    if budget < one_bread_price:
        break
    budget -= one_bread_price
    breads_count += 1
    colored_eggs_count += 3
    if breads_count % 3 == 0:
        colored_eggs_count -= (breads_count -2)
print(f"You made {breads_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
