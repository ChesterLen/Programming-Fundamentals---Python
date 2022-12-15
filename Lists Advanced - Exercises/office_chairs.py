number_of_rooms = int(input())
room_number = 0
free_chairs = 0
chairs_enough = True
for room in range(number_of_rooms):
    chairs_visitors = input().split(" ")
    room_number += 1
    chairs_quantity = len(chairs_visitors[0])
    visitors_quantity = int(chairs_visitors[1])
    if chairs_quantity > visitors_quantity:
        free_chairs += chairs_quantity - visitors_quantity
    if visitors_quantity > chairs_quantity:
        chairs_enough = False
        print(f"{visitors_quantity - chairs_quantity} more chairs needed in room {room_number}")
if chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")
