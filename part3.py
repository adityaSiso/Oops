"""Single Inheritance"""

# Overriding

# Extending

class Person:

    def __init__(self, name) -> None:
        self.name = name

    def greet(self) -> None:
        print(f'Hello {self.name}!')

    def sleep(self) -> None:
        print(f'Person {self.name} sleeps...')

    def __repr__(self) -> str:
        print(f'Person({self.name})')

class Student(Person):

    def greet(self) -> None:                # Overriding
        print(f'Yoo {self.name}!')

    def study(self) -> None:                # Extending
        print(f'Student {self.name} studies..')

    def __repr__(self) -> str:
        super().__repr__()                  # Delegating
        print(f'Student({self.name})')

# Delegating to Parent
"""calling parent using super."""

# Slots
"""Slots works on an instance level not on the class level.

class BankAccount:
    __slots__ = 'a', 'b', ...
    def __init__(self, *args, **kwargs):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.d = args[3]
        ... 10k instances

In case of 10k instance we will have some memory overhead so to avoid that we
can use slots (__slots__), which takes the instance names we want to store.

when slots are implemeted we can not use __dict__ and vars on instance level.
obj.__dict__ or vars(obj).

AND we cannot add an attribute to an instance.
obj.new = 'test'
"""

class Person:
    __slots__ = 'name',

    def __init__(self, name) -> None:
        self.name = name


class Student(Person):
    __slots__ = 'course', '__dict__'

    def __init__(self, name, course) -> None:
        super().__init__(name)
        self.course = course


# ------------------------------------------------------------------------------

def validate_integer(arg_name: str, arg_value: int,
                     min_value: int = None, max_value: int = None,):

    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} value should be of integer type.')

    if min_value is not None and arg_value < min_value:
        raise ValueError(f'{arg_value} fails the minimum bound value.')

    if max_value is not None and arg_value > max_value:
        raise ValueError(f'{arg_value} fails the maximum bound value.')


"""Project"""
class Resource:

    def __init__(self, name, manufacturer, total, allocated) -> None:
        self._name = name
        self._manufacturer = manufacturer
        validate_integer('total', total, min_value=0)
        self._total = total
        validate_integer('allocated', allocated, min_value=0, max_value=total)
        self._allocated = allocated

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (f'{self.name} ({self.category} - {self.manufacturer}) : '
                f'total={self.total}, allocated={self.allocated}')

    @property
    def name(self) -> str:
        return self._name

    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @property
    def total(self) -> int:
        return self._total

    @property
    def allocated(self) -> int:
        return self._allocated

    @property
    def available(self) -> int:
        return self._total - self._allocated

    @property
    def category(self) -> str:
        return type(self).__name__.lower()

    def claim(self, num) -> None:
        validate_integer('Claim', num, max_value=self.available, min_value=1)
        self._allocated += num

    def freeup(self, num) -> None:
        validate_integer('Freeup', num, min_value=1, max_value=self.allocated)
        self._allocated -= num

    def dies(self, num) -> None:
        validate_integer('Dies', num, min_value=1, max_value=self.allocated)
        self._total -= num
        self._allocated -= num

    def purchased(self, num) -> None:
        validate_integer('Purchased', num, min_value=1)
        self._total += num


class CPU(Resource):

    def __init__(self, name, manufacturer, total, allocated,
                 cores, socket, power_watts) -> None:
        super().__init__(name, manufacturer, total, allocated)
        validate_integer('Cores', cores, min_value=1)
        validate_integer('Power Watts', power_watts, min_value=1)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    def __repr__(self) -> str:
        return f'{self.category} : {self.name} ({self.socket} - x{self.cores})'

    @property
    def cores(self) -> int:
        return self._cores

    @property
    def socket(self) -> str:
        return self._socket

    @property
    def power_watts(self) -> int:
        return self._power_watts


class Storage(Resource):

    def __init__(self, name, manufacturer, total, allocated, capacity) -> None:
        super().__init__(name, manufacturer, total, allocated)
        validate_integer('Capacity', capacity, min_value=1)
        self._capacity = capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    def __repr__(self) -> str:
        return f'{self.category} : {self.name} {self.capacity}GB'


class HDD(Storage):

    def __init__(self, name, manufacturer, total, allocated, capacity,
                 size, rpm) -> None:
        super().__init__(name, manufacturer, total, allocated, capacity)
        allowed_sizes = ["2.5", "3.5"]
        for allowed_size in allowed_sizes:
            raise ValueError(f'{size} is a Invalid Size. '
                            f'Only {allowed_sizes} are allowed.')
        self._size = size
        validate_integer('RPM', rpm, min_value=1)
        self._rpm = rpm

    def __repr__(self) -> str:
        return f'{super().__repr__()} (Size: {self.size}, RPM: {self.rpm})'

    @property
    def size(self) -> str:
        return self._size

    @property
    def rpm(self) -> int:
        return self._rpm


class SSD(Storage):

    def __init__(self, name, manufacturer, total, allocated, capacity,
                 interface) -> None:
        super().__init__(name, manufacturer, total, allocated, capacity)
        self._interface = interface

    def __repr__(self) -> str:
        return f'{super().__repr__()} Interface: {self.interface}'

    @property
    def interface(self) -> None:
        return self._interface
