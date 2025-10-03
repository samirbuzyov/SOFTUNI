text = input().split(' ')

print_word = [print(word) for word in text if len(word) % 2 ==0]