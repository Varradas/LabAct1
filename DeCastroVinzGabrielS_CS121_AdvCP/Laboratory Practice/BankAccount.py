from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    @property
    def account_number(self):
        return self._account_number
    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= -5000:
            self._balance -= amount
            return True
        else:
            self._balance = "Withdrawal Amount Exceeds Overdraft Amount of -5000!"
    
    def display_account_type(self):
        return "Current Account"
        
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        else:
            self._balance = "Withdrawal Amount Exceeds Available Balance!"
    
    def display_account_type(self):
        return "Savings Account"

def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Account Type: {account.display_account_type()}")


# Test

if __name__ == "__main__":
    savings1 = SavingsAccount("SA123", 1200) 
    current1 = CurrentAccount("CA456", -200)
    savings2 = SavingsAccount("SA123", 1200)
    current2 = CurrentAccount("CA456", -200)
    
    savings1.withdraw(1300)# Should fail
    current1.withdraw(5000)# Should fail
    savings2.withdraw(510)
    current2.withdraw(320) 

    print_account_details(savings1)
    print("--------------------------------")
    print_account_details(current1)
    print("--------------------------------")
    print_account_details(savings2)
    print("--------------------------------")
    print_account_details(current2)
    print("--------------------------------")