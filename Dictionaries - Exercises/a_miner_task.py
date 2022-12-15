resources_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    resource_value = int(input())
    if resource not in resources_dict.keys():
        resources_dict[resource] = 0
    resources_dict[resource] += resource_value
for key, value in resources_dict.items():
    print(f"{key} -> {value}")
