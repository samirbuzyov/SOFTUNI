the_book = input()

books = input()
books_count = 0

while True:

    if books == the_book:
        print(f"You checked {books_count} books and found it.")
        break

    elif books == 'No More Books':
        print(f"The book you search is not here!")
        print(f"You checked {books_count} books.")
        break

    books_count += 1
    books = input()