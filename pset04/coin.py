class CoinPurse(object):
    def __init__(self, quarters=0, dimes=0, nickels=0, pennies=0):
        # TODO: implement me!
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies
        self.sum = self.amount()

    def amount(self):
        """ Return the amount of money as a floating point value """
        # TODO: implement me!
        return self.ret_quarters() * 0.25 + self.ret_dimes() * 0.10 + self.ret_nickels() * 0.05 + self.ret_pennies() * 0.01

# Note: I renamed these functions "ret_coin" because I wanted to eliminate
# reference errors due to attributes being named the same thing.
    def ret_quarters(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return int(self.quarters)

    def ret_dimes(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return int(self.dimes)

    def ret_nickels(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return int(self.nickels)

    def ret_pennies(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return int(self.pennies)

    # TODO: Override special functions to allow for comparing two CoinPurses
    #       >, <, >=, <=, ==, != should all compare CoinPurse amounts.

    def __eq__(self, other):
        return not self.sum.__ne__(other.sum)

    def __ne__(self, other):
        return not self.sum.__eq__(other.sum)

    def __lt__(self, other):
        return not self.sum.__ge__(other.sum)

    def __ge__(self, other):
        return not self.sum.__lt__(other.sum)

    def __le__(self, other):
        return not self.sum.__gt__(other.sum)
    
    def __gt__(self, other):
        return not self.sum.__le__(other.sum)

    # TODO: Override special functions to allow for adding two CoinPurses.
    #       You should support both + and +=.

    def __add__(self, other):
        if isinstance(self, CoinPurse) and isinstance(other, CoinPurse):
            return CoinPurse(self.quarters+other.quarters, self.dimes+other.dimes, self.nickels+other.nickels, self.pennies+other.pennies)
        else:
            NotImplemented
if __name__ == '__main__':
    x = CoinPurse(quarters=5, pennies=100)
    print "%0.2f should be 2.25" % x.amount()

    y = CoinPurse(dimes=30, nickels=10)
    print "%0.2f should be 3.50" % y.amount()

    z = CoinPurse(pennies=350)
    print "%0.2f should be 3.50" % z.amount()

    if x < y:
        print "x should be less than y"
    if y > x:
        print "y should be more than x"
    if y == z:
        print "y should equal z"
    if y <= z:
        print "y is less than or equal to z"

    combined = x + z
    print "Combined purse should have 450 pennies (has %d)" % combined.pennies

    y += x
    print "y should now have 5.75 money (has %0.2f)" % y.amount()
