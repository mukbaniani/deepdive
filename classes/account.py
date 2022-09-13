from time_zone import TimeZone
from datetime import datetime
import itertools


class Account:
    MONTHLY_INTEREST_RATE = 0.5

    def __init__(self, account_number, first_name, last_name, timezone_name, offset_hours, offset_minutes):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._time = TimeZone(timezone_name, offset_hours, offset_minutes)
        self._balance = 0
        self._conformation_number = None
        self._transaction_id = itertools.count(100)
        self._transaction_code = None
        self._transaction_type = {
            'deposit': 'D',
            'withdrawal': 'W',
            'interest_deposit': 'I',
            'declined': 'X'
        }

    @property
    def transaction_code(self):
        return self._transaction_code

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def conformation_number(self):
        return self._conformation_number

    @property
    def time(self):
        return self._time.offset

    @property
    def time_utc(self):
        return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def fullname(self):
        return f'{self._first_name} {self._last_name}'

    @property
    def balance(self):
        return self._balance

    def deposit(self, money: int):
        self._balance += money
        self.generate_conformation_number(transaction_type=self._transaction_type.get('deposit'))
        self.generate_transaction_id()

    def withdraw(self, money: int):
        if money > self.balance:
            self.generate_conformation_number(transaction_type=self._transaction_type.get(('declined')))
            self.generate_transaction_id()
            print('not enough money')
        else:
            self._balance -= money
            self.generate_transaction_id()
            self.generate_conformation_number(transaction_type=self._transaction_type.get('withdrawal'))

    def generate_conformation_number(self, transaction_type):
        self._transaction_code = transaction_type
        self._conformation_number = f'{transaction_type}-{datetime.utcnow().strftime("%Y%m%d%H%M%S")}-{self._transaction_id}'

    def monthly_interest_rate(self):
        self._balance += self._balance * self.MONTHLY_INTEREST_RATE
        self.generate_conformation_number(transaction_type=self._transaction_type.get('interest_deposit'))
        self.generate_transaction_id()

    def generate_transaction_id(self):
        self._transaction_id = next(self._transaction_id)


a = Account(account_number=1, first_name='zura', last_name='gela', timezone_name='TBC', offset_hours=4,
            offset_minutes=1)
# print(a.balance)
a.deposit(150)
a.monthly_interest_rate()
print(a.transaction_code)
print(a.conformation_number)
