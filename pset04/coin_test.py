import coin
import unittest

class TestCoinPurse(unittest.TestCase):  
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.null = coin.CoinPurse()
        self.zero = coin.CoinPurse(0,0,0,0)
        self.val1 = coin.CoinPurse(2, 4, 2, 100) #Amount 2.00
        self.val2 = coin.CoinPurse(5, 2, 1, 50) #Amount 2.00
        self.val3 = coin.CoinPurse(1, 1, 1, 1) #Amount 0.41
        self.neg1 = coin.CoinPurse(-1, -1, -1, -1)
        self.neg2 = coin.CoinPurse(1, 2, 3, -1.5)
        self.floa = coin.CoinPurse(1.5, 1.2, 2.2, 4.1)
        
    def testEmpty(self):
        self.assertEqual(self.null.quarters, self.zero.quarters)
        self.assertEqual(self.null.dimes, self.zero.dimes)
        self.assertEqual(self.null.nickels, self.zero.nickels)
        self.assertEqual(self.null.pennies, self.zero.pennies)
        self.assertEqual(self.null.amount(), self.zero.amount())

    def testOperationOrder(self):
        self.assertGreater(self.val2, self.val3, "2.00 two is not greater than 0.41")
        self.assertLess(self.val3, self.val2, "0.41 is not less than 2.00")

    def testAddEmpty(self):
        added_empty = self.null + self.zero
        self.assertEqual(added_empty.quarters, 0)
        self.assertEqual(added_empty.dimes, 0)
        self.assertEqual(added_empty.nickels, 0)
        self.assertEqual(added_empty.pennies, 0)
        self.assertEqual(added_empty.amount(), 0)

    def testAddEmptyToNonempty(self):
        added_empty2 = self.null + self.val1
        self.assertEqual(added_empty2.quarters, self.val1.quarters)
        self.assertEqual(added_empty2.dimes, self.val1.dimes)
        self.assertEqual(added_empty2.nickels, self.val1.nickels)
        self.assertEqual(added_empty2.pennies, self.val1.pennies)
        self.assertEqual(added_empty2.amount(), self.val1.amount())
        
if __name__ == '__main__':
    unittest.main()
                    
