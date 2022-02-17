import random # For shuffling the deck

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit # Diamonds, clubs, spades, hearts
        self.rank = rank # A, 2, 3, 4, ..., 10, J, Q, K
        self.value = value # Ace = 1 point, 2 = 2 points, etc.

class Deck:
    def __init__(self, suits = ["Diamonds", "Clubs", "Spades", "Hearts"], 
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]):
        self.suits = suits
        self.ranks = ranks
        self.values = values
        self.cards = [] # Hold all of our Cards
        for suit in self.suits: # Loop through suits
            for k in range(len(ranks)): # Loop through ranks/values
                new_card = Card(suit, self.ranks[k], self.values[k])
                self.cards.append(new_card)

    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self

new_deck = Deck()
new_deck.shuffle_deck()
for card in new_deck.cards:
    print(f"{card.rank} of {card.suit}")

"""
Design this game:
- two players
- Goal: get as close to a target value without going over (e.g. 50 points)
- Take turns - with the option to stop
- If a player stops, the other must keep going until beating the other player's score OR going over 
"""