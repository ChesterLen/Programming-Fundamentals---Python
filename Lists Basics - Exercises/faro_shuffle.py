deck = input().split(" ")
shuffles_count = int(input())
for shuffle in range(shuffles_count):
    shuffled_deck = []
    deck_on_two_parts = len(deck) // 2
    left_part = deck[0: deck_on_two_parts]
    right_part = deck[deck_on_two_parts::]
    for card_index in range(len(left_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])
    deck = shuffled_deck
print(deck)

