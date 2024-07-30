# Design and Implement a class representing Bank Accounts.
import numbers
import itertools
from datetime import timedelta
from datetime import datetime

class TimeZone:

    def __init__(self, name: int, offset_hours: int, offset_min: int) -> None:
        if not name or not name.strip():
            raise ValueError("Timezone name cannot be empty.")

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise TypeError("Hour Offset must be a integers.")

        if not isinstance(offset_min, numbers.Integral):
            raise TypeError("Minute Offset must be a integers.")

        if abs(offset_min) > 59:
            raise ValueError(
                "Minute offset must be b/w -59 and 59 (inclusive).")

        offset = timedelta(hours=offset_hours, minutes=offset_min)
        if (offset < timedelta(hours=-12, minutes=0) or
            offset > timedelta(hours=14, minutes=0)):
            raise ValueError("Offset must be between -12:00 and +14:00.")

        self._offset = offset
        self._offset_hours = offset_hours
        self._offset_min = offset_min

    @property
    def offset(self) -> timedelta:
        return self._offset

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, other) -> bool:
        return (isinstance(other, TimeZone) and self.name == other.name and
                    self._offset_hours == other._offset_hours and
                        self._offset_min == other._offset_min)

    def __repr__(self) -> str:
        return (f"TimeZone(name={self.name}, "
                f"offset_hours={self._offset_hours}, "
                f"offset_minute={self._offset_min})")


class BankAccount:

    TRANSACTION_COUNTER = itertools.count(100)
    _INTEREST_RATE = 7

    _TRANSACTION_CODES = {
        'deposit': 'D',
        'withdraw': 'W',
        'interest': 'I',
        'rejected': 'X'
    }

    def __init__(self, acc_num: str, f_name: str, l_name: str,
                 timezone: TimeZone = None, balance: int = 0) -> None:
        self._acc_num = acc_num      # Maybe some validations here
        self._f_name = f_name        # Maybe some validations here
        self._l_name = l_name        # Maybe some validations here

        if not timezone:
            timezone = TimeZone('UTC', 0, 0)
        self._timezone = timezone

        self._balance = float(balance)  # Maybe some validations here

    @property
    def account_number(self) -> str:
        return self._acc_num

    @property
    def first_name(self) -> str:
        return self._f_name

    @property
    def last_name(self) -> str:
        return self._l_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self.validate_and_set_name('_first_name', value, 'First Name')

    @last_name.setter
    def last_name(self, value: str) -> None:
        self.validate_and_set_name('_last_name', value, 'Last Name')

    def validate_name(self, attr_name: str, value: str, field: str) -> None:
        if not value:
            raise ValueError(f"{field} cannot be empty.")
        setattr(self, attr_name, value)

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def timezone(self) -> TimeZone:
        return self._timezone

    @timezone.setter
    def timezone(self, value: TimeZone) -> None:
        if not isinstance(value, TimeoutError):
            raise ValueError("Time Zone must be a valid TimeZone object.")

    @property
    def balance(self) -> float:
        print(f'Total Balance {self._balance}.')
        return self._balance

    @classmethod
    def get_interest_rate(cls) -> int:
        return cls._INTEREST_RATE

    @classmethod
    def set_interest_rate(cls, value: numbers.Real) -> None:
        if not isinstance(value, numbers.Real):
            raise ValueError("Interest rate must be a real number.")

        if value < 0:
            raise ValueError("Interest rate cannot be negative.")
        cls._INTEREST_RATE = value

    def make_transaction(self) -> int:
        return self.generate_confirmation_code('dummy')

    def generate_confirmation_code(self, trans_code: str) -> str:
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return (f'{trans_code}-{self.account_number}-{dt_str}-'
                f'{next(BankAccount.TRANSACTION_COUNTER)}')

    def validate_transaction_amount(self, amount, field):
        if not isinstance(amount, numbers.Real):
            raise ValueError(f"{field} amount must be a real number.")
        if amount <= 0:
            raise ValueError(f'{field} amount must be a positive number')

    def withdraw(self, amount: int):
        self.validate_transaction_amount(amount, 'Withdraw')
        if amount > self.balance:
            trans_code = BankAccount._TRANSACTION_CODES['rejected']
        else:
            trans_code = BankAccount._TRANSACTION_CODES['withdraw']
            self._balance -= amount
        conf_code = self.generate_confirmation_code(trans_code)
        return conf_code

    def deposit(self, amount: numbers.Real):
        self.validate_transaction_amount(amount, 'Deposit')
        conf_code = self.generate_confirmation_code(
            BankAccount._TRANSACTION_CODES['deposit'])
        self._balance += amount
        return conf_code

    def pay_interest(self):
        interest = self.balance * BankAccount.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(
            BankAccount._TRANSACTION_CODES['interest'])
        self._balance += interest
        return conf_code
