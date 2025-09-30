countries = input().split(', ')
capitals = input().split(', ')

dict1 = {country : capital for (country, capital) in zip(countries, capitals)}


# final_dict = dict(zip(countries,capitals))

for country, capital in dict1.items():
    print(f"{country} -> {capital}")