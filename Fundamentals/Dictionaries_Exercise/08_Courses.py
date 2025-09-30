courses = {}

while True:
    command = input()

    if command == 'end':
        break

    course_name, student_name = command.split(' : ')

    if course_name not in courses:
        courses[course_name] = []


    courses[course_name].append(student_name)



for course_name, students in courses.items():
    registered_students = len(courses[course_name])
    print(f"{course_name}: {registered_students}")
    for student in courses[course_name]:
        print(f"-- {student}")

