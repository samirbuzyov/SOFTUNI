students_name = input()

grade = 1
attempts = sum_score = 0

while True:
    if attempts > 1:
        print(f"{students_name} has been excluded at {grade} grade")
        break


    score = float(input())

    if score >= 4:
        sum_score += score
    else:
        attempts += 1
        continue



    if grade == 12:
        print(f"{students_name} graduated. Average grade: {(sum_score / 12):.2f}")
        break




    grade += 1