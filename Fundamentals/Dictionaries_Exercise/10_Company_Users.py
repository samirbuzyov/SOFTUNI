company = {}

while True:
    command = input()
    if command == 'End':
        break

    company_name, employees_id = command.split(' -> ')

    if company_name not in company:
        company[company_name] = []

    if employees_id not in company[company_name]:
        company[company_name].append(employees_id)


for company_names, id_list in company.items():
    print(f'{company_names}')
    for id in id_list:
        print(f"-- {id}")