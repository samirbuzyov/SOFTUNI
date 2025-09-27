first = int(input())
second = int(input())
third = int(input())
total = first + second + third

minutes = total // 60
seconds = total % 60

if seconds <= 9:
    print(f'{minutes}:{seconds :.02d}')
elif seconds > 9:
    print(f"{minutes}:{seconds}")