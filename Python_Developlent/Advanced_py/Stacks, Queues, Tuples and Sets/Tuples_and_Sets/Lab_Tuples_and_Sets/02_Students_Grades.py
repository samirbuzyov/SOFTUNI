students_count = int(input())

students_record = {}

for _ in range(students_count):
    data = input().split()
    name = data[0]
    grade = float(data[1])

    if name not in students_record:
        students_record[name] = []

    students_record[name].append(grade)

for student, grades in students_record.items():
    avg = sum(grades) / len(grades)
    grades_str = " ".join([f"{el:.2f}" for el in grades])
    print(f"{student} -> {grades_str} (avg: {avg:.2f})")
