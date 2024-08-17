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
