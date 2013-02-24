class CoinPurse(object):
    def __init__(self, quarters=0, dimes=0, nickels=0, pennies=0):
        # TODO: implement me!
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies

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
        return not self.amount().__ne__(other.amount())

    def __ne__(self, other):
        return not self.amount().__eq__(other.amount())

    def __lt__(self, other):
        return not self.amount().__ge__(other.amount())

    def __ge__(self, other):
        return not self.amount().__lt__(other.amount())

    def __le__(self, other):
        return not self.amount().__gt__(other.amount())
    
    def __gt__(self, other):
        return not self.amount().__le__(other.amount())

    # TODO: Override special functions to allow for adding two CoinPurses.
    #       You should support both + and +=.

    def __add__(self, other):
        if isinstance(self, CoinPurse) and isinstance(other, CoinPurse):
            return CoinPurse(self.quarters+other.quarters, self.dimes+other.dimes, self.nickels+other.nickels, self.pennies+other.pennies)
        else:
            NotImplemented
        #It seems like I don't have to override __iadd__ for +=: the function
        #works just fine with the above definitions.
            
    def __str__(self):
        coin_dict = {"quarter": self.quarters, "dime": self.dimes, "nickel": self.nickels, "penny": self.pennies}
        str_list = []
        has_penny = 0
        #Pennies are separated from the loop because if/else logic in the loop
        #was making the penny string value append out of order.
        for i in coin_dict:
            if i == "penny":
                has_penny = coin_dict[i]
            if coin_dict[i] == 1:
                if i != "penny":
                    str_list.append("%s %s" % (coin_dict[i], i))
            elif coin_dict[i] > 1:
                if i != "penny":
                    str_list.append("%s %ss" % (coin_dict[i], i))
        if has_penny == 1:
            str_list.append("%s penny" % self.pennies)
        if has_penny > 1:
            str_list.append("%s pennies" % self.pennies)
        if len(str_list) == 4:
            return "%s, %s, %s, and %s" % (str_list[0], str_list[1], str_list[2], str_list[3])
        elif len(str_list) == 3:
            return "%s, %s, and %s" % (str_list[0], str_list[1], str_list[2])
        elif len(str_list) == 2:
            return "%s and %s" % (str_list[0], str_list[1])
        elif len(str_list) == 1:
            return str_list[0]
        elif str_list == []:
            return "There are no coins in this coin purse."
        
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
    print x
    print y
    print z
    print combined
    print CoinPurse(quarters = 1, dimes = 1, nickels = 1, pennies = 1)
    print CoinPurse()
    

    
