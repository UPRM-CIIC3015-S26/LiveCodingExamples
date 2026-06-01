import random

# Immutable collections for ranks and suits
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('hearts', 'spades', 'clubs', 'diamonds')

WINNING_HANDS = (
    'High Card',
    'One Pair',
    'Two Pair',
    'Three of a Kind',
    'Straight',
    'Flush',
    'Full House',
    'Four of a Kind',
    'Straight Flush'
)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank,self.suit))

    def __str__(self):
        return f"Card: [{self.rank},{self.suit}]"

class Deck:
    def __init__(self):
        self.cards = []
        for r in RANKS:
            for s in SUITS:
                self.cards.append(Card(r,s))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def draw_hand(self, num_cards):
        hand_list = []
        for i in range(num_cards):
            hand_list.append(self.draw_card())
        return Hand(hand_list)


class Hand:
    def __init__(self, cards):
        self.cards = set(cards)

    def is_three_of_a_kind(self):
        rank_counts = {}
        for c in self.cards:
            rank_counts[c.rank] = rank_counts.get(c.rank,0) + 1
        for k in rank_counts:
            if rank_counts[k] >= 3:
                return True
        return False

    def is_full_house(self):
        rank_counts = {}
        for c in self.cards:
            rank_counts[c.rank] = rank_counts.get(c.rank,0) + 1
        rank_2 = False
        rank_3 = False
        for k in rank_counts:
            if rank_counts[k] == 3:
                rank_3 = True
            if rank_counts[k] == 2:
                rank_2 = True
        return rank_3 and rank_2


def estimate_probability_of_full_house(experiments):
    hits = 0
    for i in range(experiments):
        deck = Deck()
        deck.shuffle()
        hand = deck.draw_hand(5)
        if hand.is_full_house():
            hits += 1
    return hits/experiments

for experiments in [100, 1000, 10000, 100000, 1000000]:
    print(f"Probability of a full house estimated with {experiments} is: ",
      estimate_probability_of_full_house(experiments))


#
#
# print(Card('2','diamonds'))
#
# hand1 = Hand([Card('2','diamonds'),
#               Card('2','spades'),
#               Card('2','clubs'),
#               Card('A','diamonds')])
#
# hand2 = Hand([Card('2','diamonds'),
#               Card('3','spades'),
#               Card('2','clubs'),
#               Card('A','diamonds')])
#
# hand3 = Hand([Card('2','diamonds'),
#               Card('3','spades'),
#               Card('2','clubs'),
#               Card('2','hearts'),
#               Card('3','diamonds')])
#
# # print(hand1.is_three_of_a_kind())
# # print(hand2.is_three_of_a_kind())
# print(hand3.is_full_house())
# print(hand2.is_full_house())