def collect(items, item_):
    if item_ not in items:
        items.append(item_)


def drop(items, item_):
    if item_ in items:
        item_index = items.index(item_)
        items.pop(item_index)


def combine_items(items, old_item_, new_item_):
    if old_item_ in items:
        items.insert(items.index(old_item_) + 1, new_item_)


def renew(items, item_):
    if item_ in items:
        items.append(items.pop(items.index(item_)))


items_list = [x for x in input().split(", ")]
while True:
    command = input()
    if command == "Craft!":
        print(", ".join(items_list))
        break
    command = command.split(" - ")
    command_type = command[0]
    if command_type == "Collect":
        item = command[1]
        collect(items_list, item)
    elif command_type == "Drop":
        item = command[1]
        drop(items_list, item)
    elif command_type == "Combine Items":
        old_item, new_item = command[1].split(":")
        combine_items(items_list, old_item, new_item)
    elif command_type == "Renew":
        item = command[1]
        renew(items_list, item)
