goal_steps = 10_000
total_steps = 0
goal_is_valid = False

command = input()


while command != 'Going home':
    steps = int(command)

    total_steps += steps

    if total_steps >= goal_steps:
        goal_is_valid = True
        break

    command = input()

if command == 'Going home':
    steps = int(input())
    total_steps += steps
    if total_steps >= goal_steps:
        goal_is_valid = True


difference = goal_steps - total_steps

if goal_is_valid:
    difference = goal_steps - total_steps
    print("Goal reached! Good job!")
    print(f"{abs(difference)} steps over the goal!")

else:


    print(f"{abs(difference)} more steps to reach goal.")