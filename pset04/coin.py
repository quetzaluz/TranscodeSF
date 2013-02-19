class CoinPurse:
    def __init__(self, quarters=0, dimes=0, nickels=0, pennies=0):
        # TODO: implement me!
        pass

    def amount(self):
        """ Return the amount of money as a floating point value """
        # TODO: implement me!
        return 0

    def quarters(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return 0

    def dimes(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return 0

    def nickels(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return 0

    def pennies(self):
        """ Returns the number of quarters as an integer """
        # TODO: implement me!
        return 0

    # TODO: Override special functions to allow for comparing two CoinPurses
    #       >, <, >=, <=, ==, != should all compare CoinPurse amounts.

    # TODO: Override special functions to allow for adding two CoinPurses.
    #       You should support both + and +=.


if __name__ == '__main__':
    x = CoinPurse(quarters=5, pennies=100)
    print "%0.2f should be 2.25" % x.amount()

    y = CoinPurse(dimes=30, nickels=10)
    print "%0.2f should be 3.50" % y.amount()

    z = CoinPurse(pennies=350)

    if x < y:
        print "x should be less than y"
    if y > x:
        print "y should be more than x"
    if y == z:
        print "y should equal z"
    if y <= z:
        print "y is less than or equal to z"

    combined = x + z
    print "Combined purse should have 450 pennies (has %d)" % combined.pennies()

    y += x
    print "y should now have %0.2f money (has %0.2f)" % y.amount()
