pages_count = 899
cover_count = 2

page_price = float(input())
cover_price = float(input())

discount_paper_percent = int(input())
designer_cost = float(input())
team_contribute_percentage = int(input())


book_price = page_price * pages_count + cover_price * cover_count
discount_book = book_price- discount_paper_percent/100 * book_price
book_designer_cost = discount_book + designer_cost
total_price = book_designer_cost - team_contribute_percentage / 100 * book_designer_cost
print(f"Avtonom should pay{total_price: .2f} BGN.")