low_score_min = int(input())
exercise = input()


problem_name = ''
attempts = count_tries = sum_score = 0


while True:


    if exercise == 'Enough':
        print(f"Average score: {(sum_score / count_tries):.2f}")
        print(f"Number of problems: {count_tries}")
        print(f"Last problem: {problem_name}")
        break
    else:
        problem_name = exercise

    score = float(input())
    sum_score += score
    if score <= 4:
        attempts += 1
        if attempts == low_score_min:
            print(f"You need a break, {low_score_min} poor grades.")
            break

    count_tries += 1
    exercise = input()



