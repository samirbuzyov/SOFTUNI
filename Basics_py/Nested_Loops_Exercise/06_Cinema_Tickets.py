film_name = input()

student_ticket = 0
standard_ticket = 0
kid_tickets = 0

while film_name != 'Finish':
    seats_available = int(input())
    total_seat = seats_available

    ticket = input()
    while ticket != 'End':
        if ticket == 'student':
            student_ticket += 1
        elif ticket == 'standard':
            standard_ticket += 1
        elif ticket == 'kid':
            kid_tickets += 1

        seats_available -= 1
        if seats_available <= 0:
            break

    seats_bought = total_seat - seats_available
    percent_full = seats_bought / total_seat * 100

    print(f"{film_name} - {percent_full:.2f}% full.")


    film_name = input()
total_ticket = standard_ticket + student_ticket + kid_tickets
kid_per = kid_tickets / total_ticket * 100
standard_per = standard_ticket / total_ticket * 100
student_per = student_ticket / total_ticket * 100

if film_name == 'Finish':
    print(f"Total tickets: {total_ticket}")
    print(f"{student_per:.2f}% student tickets.")
    print(f"{standard_per:.2f}% standard tickets.")
    print(f"{kid_per:.2f}% kids tickets.")
