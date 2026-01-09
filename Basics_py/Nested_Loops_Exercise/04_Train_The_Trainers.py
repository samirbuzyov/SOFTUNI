from math import floor

jury = int(input())
name_presentation = input()

avg_presentaiton_score= 0
counter = 0
avg_total_score = 0

while name_presentation != 'Finish':

    avg_presentaiton_score = 0
    for _ in range(jury):
        grade = float(input())
        avg_presentaiton_score += grade

    avg_presentaiton_score /= jury
    print(f'{name_presentation} - {avg_presentaiton_score:.2f}.')
    avg_total_score += avg_presentaiton_score
    counter += 1

    name_presentation = input()

avg_total_score /= counter

if name_presentation == 'Finish':
    print(f"Student's final assessment is {avg_total_score:.2f}.")