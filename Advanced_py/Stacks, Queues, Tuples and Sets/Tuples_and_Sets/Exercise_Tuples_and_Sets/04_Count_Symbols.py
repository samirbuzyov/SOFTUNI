
user_inpt = input()

data = {}

info = tuple([char for char in user_inpt])
for char in sorted(info):
    if char not in data:
        data[char] = info.count(char)

for key, value in data.items():
    print(f'{key}: {value} time/s')