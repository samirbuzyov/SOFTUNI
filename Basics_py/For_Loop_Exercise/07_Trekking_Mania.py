groups_number = int(input())

mountain = ''
total_people = 0
musala = 0
monblan = 0
kilimadjaro = 0
k2 = 0
everest = 0
for _ in range(groups_number):
    people_number = int(input())
    total_people += people_number
    if people_number <= 5:
        mountain = 'musala'
        musala += people_number
    elif 5 < people_number <= 12:
        mountain = 'monblan'
        monblan += people_number
    elif 12 < people_number <=25:
        mountain = 'kilimadjaro'
        kilimadjaro += people_number
    elif 25 < people_number <=40:
        mountain = 'k2'
        k2 += people_number
    else:
        mountain = 'everest'
        everest += people_number


print(f'{musala / total_people *100:.2f}%')
print(f'{monblan / total_people * 100:.2f}%')
print(f'{kilimadjaro / total_people * 100:.2f}%')
print(f'{k2 / total_people * 100:.2f}%')
print(f'{everest / total_people * 100:.2f}%')

