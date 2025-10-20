
class BankAccount:
    balance = 0

    def add_money(self, amount):
        self.balance += amount

    def take_money(self, amount):
        x = self.balance
        try:
            if x - amount > self.min_balance:
                self.balance -= amount
                run = False
            else:
                raise ValueError()
        except ValueError:
            print("You're trying to take more than the minimum balance")

class SavingsAccoount(BankAccount):
    def __init__(self, min_limit):
        self.min_balance = min_limit

    
account = SavingsAccoount(100)

account.add_money(900)

account.take_money(850)

print(account.balance)