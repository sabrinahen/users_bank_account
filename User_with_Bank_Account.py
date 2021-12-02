class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            print(self.balance)
            
        else:
            self.balance -= amount
            print(self.balance)
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(self.balance)
        else:
            print(self.balance)
        return self

class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = { "checking" : BankAccount(0.2, 1000), "savings" : BankAccount(0.5, 3000) }

    def make_deposit(self, amount, type):
        self.account[type].deposit(amount)

    def make_withdrawl(self, amount, type):
        self.account[type].withdraw(amount)

    def display_user_balance(self, type):
        self.account[type].display_account_info()

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


michael = User("Michael Jordan", "mjchicago@gmail.com")
david = User("David Blaine", "magicdave@gmail.com")
sabrina = User("Sabrina Henrice", "bestdeveloper@gmail.com")

sabrina.make_deposit(200, "checking")
sabrina.make_withdrawl(200, "checking")
sabrina.display_user_balance("checking")
