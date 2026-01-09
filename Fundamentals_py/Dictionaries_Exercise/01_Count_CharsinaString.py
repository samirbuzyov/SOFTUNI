txt= input()
letters = {}

for char in txt:
    if char == ' ':
        continue

    if char not in letters.keys():
        letters[char] = 1
    else:
        letters[char] += 1

for char,occurrences in letters.items():
    print(f"{char} -> {occurrences}")