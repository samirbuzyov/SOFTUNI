first_sequence = input(). split(", ")
second_sequence = input(). split(", ")

substring=[]



for i in first_sequence:
    for j in second_sequence:

        if i in j:
            substring.append(i)
            break

print(substring)