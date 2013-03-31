class Account(object):
    """ One person's account """
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


atm_money = 200

# FIXME: I think this class does everything it should.  It certainly passes
# all three of my tests!  My code is perfect and can't possibly have bugs.
class EvilATM(object):
    """ An ATM machine that can turn money from an account into cash.
        There may be many ATM machines.

        This kind of ATM has the following rules:
            * Money can only be withdrawn in whole dollar amounts.
            * Withdrawing an amount less than $50 has a $5 service fee.
            * Withdrawing an amount more than $50 has a 10% service fee,
              rounded up to the nearest whole dollar.
            * As part of a temporary promotion for this bank's 17th
              anniversary, withdrawing exactly $17 has no service fee.
    """
    def __init__(self):
        # FIXME: Maybe this init function should do something...
        pass

    def cash_on_hand(self):
        """ Returns the current amount of cash this ATM has. """
        return atm_money

    def withdraw_money(self, account, amount):
        """ Tries to withdraw the amount plus the service fee from the
            account.

            If the account has enough money for the service fee plus the
            amount, this class returns a tuple of the (money withdrawn, fee).

            If the account doesn't have enough money, raise an AccountException.

            If the ATM doesn't have enough money, raise an ATMException.

            If the amount is not in whole dollars, raise an ATMException.
        """
        global atm_money  # FIXME: Not sure why I need this.
        assert(isinstance(account, Account))
        amount = float(amount)

        if amount < 50:
            fee = 5
            total = amount + fee
            if total > account.amount:
                raise AccountException(("Account cannot withdraw %f, " +
                    "it only has %f") % (amount + fee, account.amount))
            if total > self.cash_on_hand():
                raise ATMException(("ATM cannot hand out %d, " +
                    "it only has %f") % (amount + fee, self.cash_on_hand()))

            if amount == 17:  # Temporary promotion fee cancellation!
                fee = 0
        elif amount > 50:
            fee = 0.1 * amount
            total = amount + fee
            # FIXME: Oops, I was in a hurry and copy-pasted this code!
            if total > account.amount:
                raise AccountException(("Account cannot withdraw %d, " +
                    "it only has %d") % (amount + fee, account.amount))
            if total > self.cash_on_hand():
                raise ATMException(("ATM cannot hand out %d, " +
                    "it only has %d") % (amount + fee, self.cash_on_hand()))

        # In both cases, if we get here then we can actually withdraw money
        atm_money -= amount
        account.amount -= total
        return amount, fee


class ATMException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class AccountException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
