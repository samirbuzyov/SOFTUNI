command = input()

kids = 0
adults = 0
price_toys = 5
price_sweaters = 15


while command != 'Christmas':
    age = int(command)
    if age <= 16:
        kids += 1
    elif age > 16:
        adults += 1


    command = input()

total_toys = kids * price_toys
total_sweaters = adults * price_sweaters

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {total_toys}")
print(f"Money for sweaters: {total_sweaters}")