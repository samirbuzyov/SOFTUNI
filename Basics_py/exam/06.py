number_locations = int(input())


for location in range(number_locations):
    expected_yield = float(input())
    days = int(input())

    sum_gold_yield = 0
    for day in range(days):
        gold_yield = float(input())
        sum_gold_yield += gold_yield

    avg_gold_yield = sum_gold_yield / days

    if avg_gold_yield >= expected_yield:
        print(f"Good job! Average gold per day:{avg_gold_yield: .2f}.")
        continue
    elif avg_gold_yield < expected_yield:
        expected_yield -= avg_gold_yield
        print(f"You need{expected_yield: .2f} gold.")
        continue