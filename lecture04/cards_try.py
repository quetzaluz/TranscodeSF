# -*- coding: utf-8 -*-
# ^^^^^ The above is a magic comment to make unicode work.

import random


COLORS = {
    'ENDC':0,  # RESET COLOR
    'DARK_RED':31,
    'RED':91,
    'RED_BG':41,
    'YELLOW':93,
    'YELLOW_BG':43,
    'BLUE':94,
    'BLUE_BG':44,
    'PURPLE':95,
    'MAGENTA_BG':45,
    'AUQA':96,
    'CYAN_BG':46,
    'GREEN':92,
    'GREEN_BG':42,
    'BLACK':30,
}

def termcode(num):
    return '\033[%sm'%num

def colorstr(astr, color):
    return termcode(COLORS[color])+astr+termcode(COLORS['ENDC'])
HEART = "♥"
DIAMOND = "♦"
SPADE = "♠"
CLUB = "♣"

SUITS = [HEART, DIAMOND, SPADE, CLUB]
VALUES = ["2", "3", "4", "5", "6", "7", "8", 
          "9", "10", "J", "Q", "K", "A"]

class Table:
    """ Represents all cards in play at any time"""
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for j in range(2,15):
                cards.append(Card(suit, j))

    def getWholeDeck(self):
        """Return a Deck associated with this Table that has all the cards in it"""
        return self.cards 


class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __str__(self):
        ret = VALUES[self.value-2] + self.suit
        if self.suit == HEART or self.suit == DIAMOND:
            return colorstr(ret, 'RED')
        return ret

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        """Take the top card off this deck and return it"""
        return self.cards.pop()

    def shuffle(self):
        """Randomize the order of this Deck"""
        random.shuffle(self.cards)

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret = ret + str(card) + " "
        return ret

    def _isStraight(self):
        for start in range(2, 10):
            represented = 0
            ran = range(start, start + 5)
            for value in ran:
                for card in self.cards:
                    if card.value == value:
                        represented += 1
            if represented == 5:
                return True
        return False

    def _ofAKind(self, howMany):
        """ Return the value that this hand has howMany of, or None if no such value"""
        d = {}
        for card in self.cards:
            if card.value in d:
                d[card.value] += 1
            else:
                d[card.value] = 1
        for value in d:
            if d[value] == howMany:
                return value
        return None
            
# I added the following definitions for my winning hand dictionary that calls functions without arguments.
    def _twoOfAKind(self):
        return self._ofAKind(2)

    def _threeOfAKind(self):
        return self._ofAKind(3)

    def _fourOfAKind(self):
        return self._ofAKind(4)

    def _isFlush(self):
        """Return true all cards in self have the same suit"""
        for card in self.cards:
            if card.suit != self.cards[0].suit:
                return False
        return True

    def _isStraightFlush(self):
        return self._isFlush() and self._isStraight()

    def _isFullHouse(self):
        return self._ofAKind(3) is not None and self._ofAKind(2) is not None

#### My attempt at two pairs
    def _isTwoPairs(self):
        d = {}
        e = {}
        pairs = 0
        for card in self.cards:
            if card.value in d:
                d[card.value] += 1
            else:
                d[card.value] = 1
        for value in d:
            if d[value] == 2:
                pairs += 1
        for card in self.cards:
            if card.value in e:
                if e[card.value] != d[card.value]:
                    e[card.value] += 1
                else:
                    e[card.value] = 1
        for value in e:
            if e[value] == 2:
                pairs +=1
        if pairs == 2:
            return True
        else:
            return False
            
        
    def _highCard(self):
        best = self.cards[0]
        for card in self.cards:
            if card.value > best.value:
                best = card
        return best
    
    def isBetterThan(self, other):
        """
        Possible hands are:
            - High card
            - Pair
            - 2 pair
            - 3 of a kind
            - Straight
            - Flush
            - Full House            
            - 4 of a kind
            - Straight Flush
        """
###My attempt at evaluating hands.
        evalu = True
        your_hand = {"Straight Flush": self._isStraightFlush, "Four of a Kind": self._fourOfAKind, "Full House": self._isFullHouse, "Flush": self._isFlush, "Straight": self._isStraight, "Three of a Kind": self._threeOfAKind, "Pair of Pairs": self._isTwoPairs, "Pair": self._twoOfAKind, "High Card": self._highCard}
        other_hand = {"Straight Flush": other._isStraightFlush, "Four of a Kind": other._fourOfAKind, "Full House": other._isFullHouse, "Flush": other._isFlush, "Straight": other._isStraight, "Three of a Kind": other._threeOfAKind, "Pair of Pairs": other._isTwoPairs, "Pair": other._twoOfAKind, "High Card": other._highCard}
        for i in your_hand:
            if your_hand[i]() is True and other_hand[i]() is not True:
                return "You win this hand with a " + i + "!"
                break
            if your_hand[i]() is not True and other_hand[i]() is True:
                return "Your opponent wins this hand with a " + i + "!"
                break
            if your_hand[i]() is True and other_hand[i]() is True:
                if self._highCard().value > other._highCard().value:
                    return "You win this hand with a " + i + " and a high card!"
                    break
                if self._highCard().value < other._highCard().value:
                    return "Your opponent wins with a " + i + " and a high card!"
                    break
                if self._highCard().value == other._highCard().value:
                    return "Your hands are tied!"
                    break

                
            
        if len(self.cards) != 5:
            raise "Not five cards!"




h = Deck([Card(DIAMOND, 2), Card(HEART, 2), Card(CLUB, 5), Card(DIAMOND, 5), Card(SPADE, 7)])
i = h
j = Deck([Card(HEART, 9), Card(DIAMOND, 6), Card(CLUB, 6), Card(HEART, 6), Card(SPADE, 3)])

print "Comparing Identical hand..."
print h.isBetterThan(i)
print "Comparing a hand where three of a kind (other) -should- win over two pairs (self)..."
print h.isBetterThan(j)
