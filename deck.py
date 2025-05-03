import random
class Card:
    """
    A class that represents playing cards.
    The class contains the ranks and suits of a standard deck of cards.
    """
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['♠', '♣', '♦', '♥']

    def __init__(self, rank, suit):
        """
        Initialize a card with a rank and suit.
        :param: rank + suit
        :raises ValueError: if rank or suit is invalid
        """
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Get the rank of the card. It gives us access to the rank of the card.
        :return: the rank of the card
        """
        return self._rank

    @property
    def suit(self):
        """
        Get the suit of the card. It gives us access to the suit of the card.
        :return: the suit of the card
        """
        return self._suit

    def __str__(self):
        """
        Get the string representation of the card. The output when I print the card.
        :return: Rank of Suit
        """
        return self.__str__()

    def __repr__(self):
        """
        Get the string representation of the card. The output when I print the card.
        :return: self.__str__()
        """
        return f"{self._rank} {self._suit}"

    def __eq__(self, other):
        """
        Check if two cards are equal. Cards are equal if they have the same rank.
        :param other:
        :return: True or False
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Check if the rank of this card is less than the rank of another card. One card is less than another if its rank is less than the other card's rank.
        :param other:
        :return: True or False
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    """
    A class that represents a deck of cards.
    The class contains a list of cards and methods to shuffle and deal cards.
    """
    def __init__(self):
        """
        Initialize a deck of cards. Combines all the ranks and suits to create a deck of 52 cards.
        """
        self._cards = [Card(r, s) for r in Card.RANKS for s in Card.SUITS]

    @property
    def cards(self):
        """
        Get the list of cards in the deck. It gives us access to the cards in the deck.
        :return: self._cards
        """
        return self._cards

    def __str__(self):
        """
        Get the string representation of the deck. The output when I print the deck.
        :return: self._cards. It gives us the list of cards in the deck. The output when I print the deck is from the Card class.
        """
        return str(self._cards)

    def shuffle(self):
        """
        Shuffle the deck of cards. It shuffles the deck of cards using the random module.
        :return:
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Deal a card from the deck. It removes the first card from the deck and returns it.
        :return: It returns the first card of the deck and removes it from the deck.
        """
        return self.cards.pop(0)


    def __len__(self):
        """
        Get the number of cards in the deck. It gives us the number of cards in the deck.
        :return: Number of cards in the dec
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        Get the card at the specified position in the deck. It gives us access to the card at the specified position in the deck.
        :param position:
        :return: The position of cards in the deck.
        """
        return self._cards[position]


if __name__ == '__main__':
    """
    If we run this file, it will create a card and a deck of cards but if it run from another file it will not
    """
    c1 = Card('A', '♠')
    print(c1)
    print(c1.suit)
    deck = Deck()
    print(deck.cards)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)