# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. Понеже Жоро предпочита да играе с приятели навън, вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя, за да прочете необходимата литература.
# Вход
# От конзолата се четат 3 реда:
#     1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#     2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#     3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
# Изход
# Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
from math import floor


number_of_pages_in_current_book = int(input())
number_of_pages_for_an_hour = int(input())
number_Of_days_to_read_a_book = int(input())

result = number_of_pages_in_current_book / number_of_pages_for_an_hour / number_Of_days_to_read_a_book

print(floor(result))

# vtori nachin
number_of_pages_in_current_book = int(input())
number_of_pages_for_an_hour = int(input())
number_Of_days_to_read_a_book = int(input())

result = number_of_pages_in_current_book / number_of_pages_for_an_hour / number_Of_days_to_read_a_book
print(int(result))

# treti nachin
number_of_pages_in_current_book = int(input())
number_of_pages_for_an_hour = int(input())
number_Of_days_to_read_a_book = int(input())

result = number_of_pages_in_current_book // number_of_pages_for_an_hour // number_Of_days_to_read_a_book
print(result)