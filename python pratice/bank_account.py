import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def show_transaction_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name  # this is public attribute
        self.balance = balance  # this is public attribute
        self.__txt = 'this private attribute'
        self._txt = 'this protected attribute'

        # by another way, when add _ or __ for the variable it is called name mangling

        print('Account created for {}'.format(self.name))
        print('The process time is', Account.show_transaction_time())

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('The process time is', Account.show_transaction_time())
        else:
            print('Invalid')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print('Withdraw process completed successfully')
            print('The process time is', Account.show_transaction_time())
        else:
            print('Your balance is not enough')

    def show_balance(self):
        print('You have $ {} in your balance'.format(self.balance))


te = Account('ahmed', 0)
te.deposit(10000)
te.show_balance()

