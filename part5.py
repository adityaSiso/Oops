"""Enumerations

Once enum has been declared

+ Mumbers list is immutable
+ Member values are immutable
+ Cannot be subclassed.
    + unless it contains no members
"""
from enum import Enum

class Consts(Enum):

    ONE = 1
    TWO = 2
    THREE = 3

try:
    class NewConsts(Enum): # This will not work.

        TEN = 10
        HUNDRED = 100
except TypeError as e:
    print(f'Enum class can not be subclasses. error: {str(e)}.')

try:
    Consts.ONE = '1'
except AttributeError as e:
    print(f'Members values can not be modified. error: {str(e)}')

"""Aliases"""
import enum

@enum.unique
class Integers(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    EK = 1
    DO = 2
    TEEN = 3

list(Integers) #[ONE, TWO, and THREE] this is because of aliases.

Integers.__members__
# {
    # 'ONE': <Integers.ONE: 1>,
    # 'TWO': <Integers.TWO: 2>,
    # 'THREE': <Integers.THREE: 3>,
    # 'EK': <Integers.ONE: 1>,
    # 'DO': <Integers.TWO: 2>,
    # 'TEEN': <Integers.THREE: 3>
# }

"""Note: we can keep the uniqueness to our enum class is by defining a
   enum.unique decorator.
"""

# Enumeration Project

class AppException:

    def __new__(cls, code, exception_class, message):
        instance = object.__new__(cls)

        instance._value_ = code
        instance.exception = exception_class
        instance.message = message

        return instance

    @property
    def code(self):
        return self.value

    def throw(self, message=None):
        return self.exception(f'{self.code} - {message or self.message}')

    NotAnInteger = 100, ValueError, 'Deno can not be zero.'


