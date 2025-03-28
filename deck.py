import random
class Card:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['♠', '♣', '♦', '♥']

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self._rank} of {self._suit}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        self._cards = [Card(r, s) for r in Card.RANKS for s in Card.SUITS]

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self.cards.pop(0)


    # def __len__(self):
    #     return len(self._cards)
    #
    # def __getitem__(self, position):
    #     return self._cards[position]


if __name__ == '__main__':
    c1 = Card('A', '♠')
    print(c1)
    print(c1.suit)
    deck = Deck()
    print(deck.cards)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)