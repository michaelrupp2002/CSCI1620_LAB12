import unittest
from account import *


class TestAccount(unittest.TestCase):


    def setUp(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

    def tearDown(self):
        del self.a1
        del self.a2

    def test_init(self):
        self.assertEqual(self.a1.get_name(), 'John')
        self.assertEqual(self.a1.get_balance(), 0)
        self.assertEqual(self.a2.get_name(), 'Jane')
        self.assertEqual(self.a2.get_balance(), 0)

    def test_deposit(self):
        assert self.a1.deposit(10.0) is True
        self.assertEqual(self.a1.get_balance(), 10.0)
        assert self.a2.deposit(0) is False
        self.assertEqual(self.a2.get_balance(), 0)
        assert self.a1.deposit(-15.0) is False
        self.assertEqual(self.a1.get_balance(), 10.0)

    def test_withdraw(self):
        assert self.a1.deposit(10.0) is True
        assert self.a1.withdraw(5.0) is True
        self.assertEqual(self.a1.get_balance(), 5.0)
        assert self.a1.withdraw(10.0) is False
        self.assertEqual(self.a1.get_balance(), 5.0)
        assert self.a2.withdraw(-10) is False
        self.assertEqual(self.a2.get_balance(), 0)


if __name__ == '__main__':
    unittest.main()
