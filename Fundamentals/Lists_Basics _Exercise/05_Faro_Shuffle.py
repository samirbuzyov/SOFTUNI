card_deck = input().split()
faro_shuffles = int(input())

deck = []
for i in card_deck:
    temp = i
    deck.append(temp)


for i in range(faro_shuffles):
    new_deck = []
    for i in range(0,len(deck)//2):
        new_deck.append(deck[i])
        for j in range(len(deck)//2, len(deck)):
            if j -len(deck) //2 == i:
                new_deck.append(deck[j])
                break
    deck = new_deck
print(deck)

