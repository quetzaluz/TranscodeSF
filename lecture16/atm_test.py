from atm import *
import unittest

# FIXME: All these tests pass, but maybe we should write some more.

class ATMUnitTest(unittest.TestCase):
    def test_small_withdraw(self):
        account = Account("enne", 200.00)
        atm = EvilATM()

        # Try to withdraw 5 dollars.  This should have a $5 service fee.
        withdrawn, fee = atm.withdraw_money(account, 5.00)
        self.assertEqual(withdrawn, 5.00)
        self.assertEqual(fee, 5.00)
        self.assertEqual(account.amount, 190.00)

    def test_big_withdraw(self):
        # Try to withdraw 100 dollars.  This should have a $10 service fee.
        account = Account("enne", 200.00)
        atm = EvilATM()

        withdrawn, fee = atm.withdraw_money(account, 100.00)
        self.assertEqual(withdrawn, 100.00)
        self.assertEqual(fee, 10.00)
        self.assertEqual(account.amount, 90.00)

    def test_promotion(self):
        # Try to withdraw 17 dollars, there should be no fee.
        account = Account("enne", 200.00)
        atm = EvilATM()

        withdrawn, fee = atm.withdraw_money(account, 17)
        self.assertEqual(withdrawn, 17)
        self.assertEqual(fee, 0)

    def test_fifty(self):
        # Try to withdraw 50 dollars, there should be a $5 fee.
        account = Account("enne", 200.00)
        atm = EvilATM()

        withdrawn, fee = atm.withdraw_money(account, 50)
        self.assertEqual(withdrawn, 50)
        self.assertEqual(fee, 5)
        self.assertEqual(account.amount, 145)

    def test_too_little_in_account(self):
        #Try to withdraw more than is in account. Should raise an AccountException.
		account = Account("enne", 200.00)
        atm = EvilATM()
 
        self.assertRaises(AccountException, atm.withdraw_money(account, 200))

    def test_too_little_in_ATM(self):
        #Try to withdraw more than is in the ATM  
        account = Account("enne", 3200.00)
        atm = EvilATM()

        self.assertRaises(ATMException, atm.withdraw_money(account, 201))



    
		

		


	

if __name__ == "__main__":
    unittest.main()

"""NOTES ABOUT OTHER BUGS TO CATCH:
	- Printing account.amount returns the number with only one decimal space.
	- Same goes for printing 'withdrawn' and 'fee'. Withdrawn is a float with one decimal space and 'fee' seems to be a whole integer.
	- Overdrawing
	- Withdrawing 0
	- Withdrawing negative values
	- Non-integer and non-float values.
	- Two ATMS and one account.
  - whole integers
	"""
