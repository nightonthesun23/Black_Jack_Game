import random

# deck of cards / player dealer hand 
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10, 'J', 'Q','K','A','J', 'Q','K','A','J', 'Q','K','A','J', 'Q','K','A']
playerHand = []
dealerHand = []

# deal the cards 
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
# calculate the total of each hand 
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in rane(1, 11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
# check for winner

# game loop 

