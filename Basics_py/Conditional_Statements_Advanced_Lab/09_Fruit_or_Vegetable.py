product = input()
# banana, apple, kiwi, cherry, lemon и grapes;

# еленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;



if product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' or product == 'grapes' or product == 'banana':
    print('fruit')

elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    print('vegetable')

else: 
    print('unknown')