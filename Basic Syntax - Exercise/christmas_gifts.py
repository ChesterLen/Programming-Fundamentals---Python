command = input()
kids_count = 0
adults_count = 0
toy_price = 5
sweater_price = 15
total_price_toys = 0
total_price_sweaters = 0
total_kids = 0
total_adults = 0
while command != "Christmas":
    person = int(command)
    if person <= 16:
        total_price_toys += toy_price
        total_kids += 1
    elif person > 16:
        total_price_sweaters += sweater_price
        total_adults += 1
    command = input()
print(f"Number of adults: {total_adults}")
print(f"Number of kids: {total_kids}")
print(f"Money for toys: {total_price_toys}")
print(f"Money for sweaters: {total_price_sweaters}")
