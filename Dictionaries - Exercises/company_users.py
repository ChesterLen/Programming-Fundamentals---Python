company_users_dict = {}
command = input()
while True:
    if command == "End":
        break
    command = command.split(" -> ")
    company_name = command[0]
    employee_id = command[1]
    if company_name not in company_users_dict.keys():
        company_users_dict[company_name] = []
    if employee_id not in company_users_dict[company_name]:
        company_users_dict[company_name].append(employee_id)
    command = input()
for company, employees in company_users_dict.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
