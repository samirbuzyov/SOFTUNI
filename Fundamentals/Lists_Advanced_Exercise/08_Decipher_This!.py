secret_message = input().split(' ')
newlst = []

for word in secret_message:
    num_part = ''

    if word[:3].isdigit():
        num_part = word[:3]
        word = word[3:]
    else:
        num_part = word[:2]
        word = word[2:]

    if len(word) > 1:
        word = word[-1] + word[1:-1] + word[0]
    decoded_word = chr(int(num_part)) + word
    newlst.append(decoded_word)

print(" ".join(newlst))
