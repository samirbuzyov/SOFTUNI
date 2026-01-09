breed = input()
male_female = input()
is_valid = True
life_span = 0

if breed == "British Shorthair":
    life_span = 13
elif breed == "Siamese":
    life_span = 15
elif breed == "Persian":
    life_span = 14
elif breed == 'Ragdoll':
    life_span = 16
elif breed == 'American Shorthair':
    life_span = 12
elif breed == 'Siberian':
    life_span = 11
else:
    is_valid = False
    print(f'{breed} is invalid cat!')

if male_female == 'f':
    life_span += 1
elif male_female == 'm':
    life_span += 0
else:
    print()


cat_in_human_years = life_span
cat_in_human_months = cat_in_human_years * 12
cat_months = cat_in_human_months / 6
if is_valid:
    print(f"{cat_months:.0f} cat months")