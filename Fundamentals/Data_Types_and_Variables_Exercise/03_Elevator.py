n = int(input())

p= int(input())
courses = 0

if p >= n:
    courses +=1

else:
    course_full = n // p
    course_not_full = n%p

    if course_not_full == 0:
        courses += course_full

    else:
        courses += course_full + 1


print(courses)
