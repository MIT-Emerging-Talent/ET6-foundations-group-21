import unittest
from solutions.ATM import ATM, authenticate_user, deposit_cash, withdraw_cash

class TestATM(unittest.TestCase):

    def setUp(self):
        # This is where we set up the test data, similar to the accounts in the ATM program
        self.accounts = {
            "1000717569": {"pin": "182963", "balance": 22000},
            "1000712483": {"pin": "248695", "balance": 50000},
            "1000714218": {"pin": "794587", "balance": 48233},
            "1000712487": {"pin": "332475", "balance": 10000},
            "1000715562": {"pin": "647812", "balance": 500},
            "1000713377": {"pin": "220154", "balance": 3},
        }
    
    def test_authenticate_user_success(self):
        # Test that authentication works correctly when valid details are given
        user = authenticate_user(self.accounts)
        self.assertIsNotNone(user)
    
    def test_authenticate_user_failure(self):
        # Test that authentication fails when invalid details are given
        # Simulate incorrect card number and PIN
        self.accounts["1234567890"] = {"pin": "000000", "balance": 0}
        user = authenticate_user(self.accounts)
        self.assertIsNone(user)
    
    def test_check_balance(self):
        # Test checking balance
        user = "1000717569"  # Example user
        self.assertEqual(check_balance(self.accounts, user), "Your balance is: $22000")
    
    def test_deposit_cash(self):
        # Test depositing money into the account
        user = "1000717569"
        initial_balance = self.accounts[user]["balance"]
        deposit_cash(self.accounts, user)
        self.assertGreater(self.accounts[user]["balance"], initial_balance)
    
    def test_withdraw_cash_success(self):
        # Test withdrawing money from the account (successful case)
        user = "1000717569"
        initial_balance = self.accounts[user]["balance"]
        withdraw_cash(self.accounts, user)
        self.assertLess(self.accounts[user]["balance"], initial_balance)
    
    def test_withdraw_cash_failure(self):
        # Test withdrawing more money than available (failure case)
        user = "1000713377"  # User with low balance
        initial_balance = self.accounts[user]["balance"]
        withdraw_cash(self.accounts, user)
        self.assertEqual(self.accounts[user]["balance"], initial_balance)  # Balance shouldn't change

if __name__ == "__main__":
    unittest.main()
