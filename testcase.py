import unittest
from main import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.acc1 = BankAccount("Alice", 1000)
        self.acc2 = BankAccount("Bob", 500)

    def test_initial_balance(self):
        self.assertEqual(self.acc1.get_balance(), 1000)
        self.assertEqual(self.acc2.get_balance(), 500)

    def test_deposit(self):
        self.acc1.deposit(200)
        self.assertEqual(self.acc1.get_balance(), 1200)

    def test_withdraw(self):
        self.acc1.withdraw(200)
        self.assertEqual(self.acc1.get_balance(), 800)

    def test_transfer(self):
        self.acc1.transfer(self.acc2, 300)
        self.assertEqual(self.acc1.get_balance(), 700)
        self.assertEqual(self.acc2.get_balance(), 800)

    def test_insufficient_balance_transfer(self):
        self.assertFalse(self.acc1.transfer(self.acc2, 2000))

    def test_withdraw_negative_amount(self):
        self.assertFalse(self.acc1.withdraw(-200))

    def test_deposit_negative_amount(self):
        self.assertFalse(self.acc1.deposit(-200))

    def test_transfer_negative_amount(self):
        self.assertFalse(self.acc1.transfer(self.acc2, -200))

    def test_transfer_zero_amount(self):
        self.assertFalse(self.acc1.transfer(self.acc2, 0))

    def test_account_str(self):
        self.assertEqual(str(self.acc1), "Account Holder: Alice, Balance: $1000")
        self.assertEqual(str(self.acc2), "Account Holder: Bob, Balance: $500")

    def test_set_balance(self):
        self.acc1.set_balance(1500)
        self.assertEqual(self.acc1.get_balance(), 1500)

    def test_change_holder_name(self):
        self.acc1.change_holder_name("Carol")
        self.assertEqual(self.acc1.account_holder, "Carol")

    def test_close_account(self):
        self.acc1.close_account()
        self.assertEqual(self.acc1.get_balance(), 0)
        self.assertEqual(self.acc1.account_holder, "Closed Account")

if __name__ == '__main__':
    unittest.main()
