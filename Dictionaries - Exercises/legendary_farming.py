elements_dict = {"shards": 0, "fragments": 0, "motes": 0}
item_obtained = False
elements = input().split()
while True:
    for i in range(0, len(elements), 2):
        key = elements[i + 1].lower()
        value = int(elements[i])
        if key not in elements_dict.keys():
            elements_dict[key] = 0
        elements_dict[key] += value
        if elements_dict["shards"] >= 250:
            elements_dict[key] -= 250
            item_obtained = True
            print("Shadowmourne obtained!")
        elif elements_dict["fragments"] >= 250:
            elements_dict[key] -= 250
            item_obtained = True
            print("Valanyr obtained!")
        elif elements_dict["motes"] >= 250:
            elements_dict[key] -= 250
            item_obtained = True
            print("Dragonwrath obtained!")
        if item_obtained:
            break
    if item_obtained:
        break
    elements = input().split()
for material, quantity in elements_dict.items():
    print(f"{material}: {quantity}")
