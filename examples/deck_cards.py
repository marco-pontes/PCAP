import random


class Deck:
    __suits = ['hearts', 'diamonds', 'clubs', 'spades']
    __values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.__suits for value in Deck.__values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        return [c.present() for c in self.cards]


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def present(self):
        return f'{self.value} of {self.suit}'