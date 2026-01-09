card_deck = input().split(', ')

add_cards = int(input())

for i in range(add_cards):
    command = input().split(', ')
    comm = command[0]

    if comm == 'Add':
        card = command[1]
        if card in card_deck:
            print("Card is already in the deck")
        else:
            card_deck.append(card)
            print("Card successfully added")


    elif comm == 'Remove':
        card = command[1]
        if card not in card_deck:
            print("Card not found")
        else:
            card_deck.remove(card)
            print("Card successfully removed")

    elif comm == 'Remove At':
        idx = int(command[1])
        if 0 <= idx < len(card_deck):
            card_deck.pop(idx)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif comm == 'Insert':
        card=command[2]
        idx = int(command[1])
        if idx < 0 or idx >= len(card_deck):
            print("Index out of range")
        elif 0<=idx < len(card_deck):
            if card in card_deck:
                print("Card is already added")
            elif card not in card_deck:
                card_deck.insert(idx, card)
                print("Card successfully added")


print(', '.join(card_deck))
