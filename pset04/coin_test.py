import coin
import unittest

class TestCoinPurse(unittest.TestCase):  
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.null = coin.CoinPurse()
        self.zero = coin.CoinPurse(0,0,0,0)
        self.val1 = coin.CoinPurse(2, 4, 2, 100) #Amount 2.00
        self.val2 = coin.CoinPurse(5, 2, 3, 40) #Amount 2.00
        self.val3 = coin.CoinPurse(1, 1, 1, 1) #Amount 0.41
        
    def testEmptyAndNullPurse(self):
        self.assertEqual(self.null.quarters, self.zero.quarters)
        self.assertEqual(self.null.dimes, self.zero.dimes)
        self.assertEqual(self.null.nickels, self.zero.nickels)
        self.assertEqual(self.null.pennies, self.zero.pennies)
        self.assertEqual(self.null.amount(), self.zero.amount())

    def testAddEmptyToEmpty(self):
        added1 = self.null + self.zero
        self.assertEqual(added1.quarters, 0)
        self.assertEqual(added1.dimes, 0)
        self.assertEqual(added1.nickels, 0)
        self.assertEqual(added1.pennies, 0)
        self.assertEqual(added1.amount(), 0)

    def testAddEmptyToNonempty(self):
        added2 = self.null + self.val1
        self.assertEqual(added2.quarters, self.val1.quarters)
        self.assertEqual(added2.dimes, self.val1.dimes)
        self.assertEqual(added2.nickels, self.val1.nickels)
        self.assertEqual(added2.pennies, self.val1.pennies)
        self.assertEqual(added2.amount(), self.val1.amount())
        
    def testAddNonemptyToNonempty(self):
        added3 = self.val1 + self.val2 + self.val3
        self.assertEqual(added3.quarters, 8)
        self.assertEqual(added3.dimes, 7)
        self.assertEqual(added3.nickels, 6)
        self.assertEqual(added3.pennies, 141)
        self.assertEqual(added3.amount(), 4.41)

    def testCompareSameAmountDiffCoins(self):
        self.assertNotEqual(self.val1.quarters, self.val2.quarters)
        self.assertNotEqual(self.val1.dimes, self.val2.dimes)
        self.assertNotEqual(self.val1.nickels, self.val2.nickels)
        self.assertNotEqual(self.val1.pennies, self.val2.pennies)
        self.assertEqual(self.val1.amount(), self.val2.amount())

    def testCompareDiffCoinsAndAmounts(self):
        self.assertNotEqual(self.val2.quarters, self.val3.quarters)
        self.assertNotEqual(self.val2.dimes, self.val3.dimes)
        self.assertNotEqual(self.val2.nickels, self.val3.nickels)
        self.assertNotEqual(self.val2.pennies, self.val3.pennies)
        self.assertNotEqual(self.val2.amount(), self.val3.amount())

    def testOperationOrder(self):
        self.assertGreater(self.val2, self.val3)
        self.assertTrue(self.val2 > self.val3)
        self.assertLess(self.val3, self.val2)
        self.assertTrue(self.val3 < self.val2)
       
    def testBadPurseParameters(self):
        self.assertRaises(ValueError, coin.CoinPurse, 1.5, 1.2, 2.2, 4.1)
        self.assertRaises(ValueError, coin.CoinPurse, 0, 'lol', 1, 1)
        self.assertRaises(ValueError, coin.CoinPurse, 0, 10000, -1, 3)
        self.assertRaises(ValueError, coin.CoinPurse, 1,1,1,self.val2)

    def testRemoveMoney(self):
        self.assertIsNone(self.val3.remove_money(self.val2.amount())) #Cannot subtract the value of a purse that is more than self.amount().
        self.assertTrue(self.val2.remove_money(1.0495)) # CAN subtract floats with more than two decimals thanks to rounding--think gasoline prices.
        self.assertIsNone(self.val2.remove_money(50.0005)) #Cannot subtract values larger than purse amount.
        self.assertIsNone(self.val2.remove_money(-1.00)) #Cannot subtract negative values.
        self.assertIsNone(self.val2.remove_money('butts')) #Cannot subtract string values.
        self.assertIsNone(self.val2.remove_money(self.val3)) #Cannot subtract objects
        self.assertTrue(self.val1.remove_money(2)) #CAN subtract integers less than purse amount.
        self.assertIsNone(self.val2.remove_money(100)) #Cannot subtract integers larger than purse amount.
    
        
if __name__ == '__main__':
    unittest.main()
                    
