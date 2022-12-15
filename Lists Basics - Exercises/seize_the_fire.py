fire_and_cells = input().split("#")
water_needed = int(input())
total_effort = 0
total_fire = 0
cells_put_out = []
for fire_cell in fire_and_cells:
    fire_cell_split = fire_cell.split(" = ")
    water_poured = int(fire_cell_split[1])
    fire_type = fire_cell_split[0]
    valid = False
    if water_needed < water_poured:
        continue
    if fire_type == "High":
        if 81 <= water_poured <= 125:
            valid = True
    elif fire_type == "Medium":
        if 51 <= water_poured <= 80:
            valid = True
    elif fire_type == "Low":
        if 1 <= water_poured <= 50:
            valid = True
    if valid:
        cells_put_out.append(water_poured)
        water_needed -= water_poured
        total_effort += water_poured * 25 / 100
        total_fire += water_poured
print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
