"""Polymorphism"""

# dunder methods or special methods
"""
__init__    -> class instantiation.
__enter__   -> context managers.
__exit__    -> context managers.
__setitem__ -> sequence types.
__getitem__ -> sequence types.
__delitem__ -> sequence types.
__iter__    -> iterables and iterators
__next__    -> iterables and iterators
__len__     -> implements len()
__contains__ -> implements in
.
.
.
"""

# ------------------------------------------------------------------------------
"""__str__ and __repr__ methods"""
# Both are used to generate a string representation of a object.

class Test:

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return '---'.join(self.name.split())

    def __str__(self) -> str:
        return (f'First Name: {self.name.split()[0]}, '
                f'Last Name: {self.name.split()[-1]}')

obj = Test('Young Lampost')
print(obj)      # Will call the __str__ method
x = str(obj)    # Will call the __str__ method
y = repr(obj)   # Will call the __repr__ method

# if __str__ is not implemented print and str will look __repr__ method.
# and if __repr__ is not there then the default dunder methods will be used of
# the Object class.

# if __repr__ is not implemented then object representation will implement
# the default __repr__ method.

# All the formatting ways (f, .format(), %s) will also call the __str__ method
# if implemented else __repr__ method.


# ------------------------------------------------------------------------------
"""
# Arithemetic Operators
__add__         +           # a.__add__(b)
__sub__         -
__mul__         *
__truediv__     /
__floordiv__    //
__mod__         %
__pow__         **
__matmul__      @           # Matrix multiplication for numpy.

# Reflective Operators
__radd__         +          # b.__add__(a)
__rsub__         -
__rmul__         *
__rtruediv__     /
__rfloordiv__    //
__rmod__         %
__rpow__         **

# In-place Operators
__iadd__         +=
__isub__         -=
__imul__         *=
__itruediv__     /=
__ifloordiv__    //=
__imod__         %=
__ipow__         **=

# Unary Operators
__neg__         -a
__pos__         +a
__abs__         abs(a)
"""

# ------------------------------------------------------------------------------
"""
# Rich Comparisons

__lt__          <   less than
__gt__          >   greater than
__ge__          >=  greater than equal
__le__          <=  less than equal
__eq__          ==  equal
__ne__          !=  not equal
"""

# ------------------------------------------------------------------------------
"""Hashability and Equality"""

# __hash__ and __set__
# if __eq__ is overridden in a class then class object will become unhashable
# unless __hash__ is explicitly impletemented.
class Person:

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Test) and self.name == __o.name

    def __hash__(self) -> int:
        return hash(self.name)

p1 = Person('abc')
p2 = Person('abc')
p3 = Person('xyz')

"""
p1 == p2 will be false if __eq__ was not implemented because `==` = `is` when
comparing objects but in our case it will be true as the name is being compared.
"""


# ------------------------------------------------------------------------------
"""Boolean

__bool__ = (len() == 0)
If __len__ is implemented in our class and we call bool on your object it will
simply call the __len__ method of our class.
"""

class Length:

    def __init__(self, length: str) -> None:
        self.length = length

    def __len__(self) -> bool:
        print('Calling __len__...')
        return len(self.length)

len1 = Length('abcd')
print(bool(len1)) # Calling __len__... True
len2 = Length('')
print(bool(len2)) # Calling __len__... False
