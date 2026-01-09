# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) -
# въведени от потребителя и проверява дали офисът на фирма е 
# отворен, като работното време на офисът е от 10-18 часа, от понеделник 
# до събота включително


hour = int(input())
day = input()

result = ''

if 10 <= hour <= 18:
    if day == 'Monday'or day == 'Tuesday'\
        or day == 'Wednesday'or day == 'Friday'\
        or day == 'Thursday'or day == 'Saturday':
        result = "open"
    else:
        result = "closed"

else:
    result = "closed"

print(result)