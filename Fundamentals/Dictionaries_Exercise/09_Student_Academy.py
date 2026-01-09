n = int(input())
student_dict = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in student_dict:
        student_dict[name] = {"total": 0, "count": 0}

    student_dict[name]["total"] += grade
    student_dict[name]["count"] += 1

for name, data in student_dict.items():
    average = data['total'] / data["count"]
    if average >= 4.5:
        print(f'{name} -> {average:.2f}')
