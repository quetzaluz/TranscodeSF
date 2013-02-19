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
                self.cards.append(Card(suit, j))

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
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def draw(self):
        """Take the top card off this deck and return it"""
        return self.cards.pop()

    def add(self, card):
        self.cards.append(card)

    def shuffle(self):
        """Randomize the order of this Deck"""
        random.shuffle(self.cards)

    def size(self):
        return len(self.cards)

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret = ret + str(card) + " "
        return ret

    def _isTwoPair(self):
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
        return pairs == 2


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
        return self._ofAKind(3) and self._ofAKind(2)

    def _highCard(self):
        best = self.cards[0]
        for card in self.cards:
            if card.value > best.value:
                best = card
        return best

    def _valueOfHand(self):
        if self._isStraightFlush():
            return 8
        elif self._ofAKind(4):
            return 7
        elif self._isFullHouse():
            return 6
        elif self._isFlush():
            return 5
        elif self._isStraight():
            return 4
        elif self._ofAKind(3):
            return 3
        elif self._ofAKind(2):
            return 2
        else:
            return 1


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
        return self._valueOfHand() > other._valueOfHand()

def populateHand(receiving, giving):
    while receiving.size() < 5:
        receiving.add(giving.draw())

def main():
    table = Table()
    player_1_hand = Deck()
    player_2_hand = Deck()
    total_deck = Deck(table.getWholeDeck())
    total_deck.shuffle()
    populateHand(player_1_hand, total_deck)
    populateHand(player_2_hand, total_deck)
    print "Player 1 hand", player_1_hand
    print "Player 2 hand", player_2_hand
    if player_1_hand.isBetterThan(player_2_hand):
        print "Congradulations player 1, you win!"
    else:
        print "Go player 2, you win!"


main()

