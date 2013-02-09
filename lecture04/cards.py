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

    def _isFlush(self):
        """Return true all cards in self have the same suit"""
        for card in self.cards:
            if card.suit != self.cards[0].suit:
                return False
        return True

    def _isStraightFlush(self):
        return self._isFlush() and self._isStraight()

    def _isFullHouse(self):
        return self._ofAKind(3) is not None and 
            self._ofAKind(2) is not None

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
        if len(self.cards) != 5:
            raise "Not five cards!"





h = Deck([Card(DIAMOND, 3), Card(SPADE, 3), Card(HEART, 3), Card(CLUB, 6), Card(HEART, 5)])
j = Deck([Card(HEART, 4), Card(SPADE, 5), Card(DIAMOND, 8), Card(CLUB, 8), Card(HEART, 8)])
print h._isFullHouse()
print j._isFullHouse()