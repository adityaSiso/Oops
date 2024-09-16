"""Descriptors"""

from random import choice
from typing import Any

class Choice:

    def __init__(self, *choices) -> None:
        self.choices = choices

    def __get__(self, instance, owner_class) -> Any: # This is a non-data discriptor.
        return choice(self.choices)

    def __set__(self, instance, value) -> None: # This is a data discriptor.
        pass

class Deck:
    suit = Choice(('Spade', 'Hearts', 'Club', 'Diamonds'))
    card = Choice(*'23456789JKQA', '10')

my_card = Deck() # 5 Clubs


class Person:

    def __init__(self, age) -> None:
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

p = Person(25)

# age = property(age)
p.age # 25

# age = age.setter(age)
p.age = 30





class Int:

    def __init__(self, min_value=None, max_value=None) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Should be Ingegral Value.")

        if self.min_value is not None and value < self.min_value:
            raise f"{self.name} should be greater than {self.min_value}."

        if self.max_value is not None and value > self.max_value:
            raise f"{self.name} should be lesser than {self.max_value}."

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self

        else:
            return instance.__dict__.get(self.name, None)

class Point2D:

    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=600)

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return ValueError(f'Point2D(x={self.x}, y={self.y})')

    def __str__(self) -> str:
        return ValueError(f'({self.x}, {self.y})')


import collections

class Point2DSequence:

    def __init__(self, min_length=None, max_length=None) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, collections.abc.Sequence):
            raise ValueError("Should be Ingegral Value.")

        if self.min_length is not None and value < self.min_length:
            raise ValueError(f"{self.name} must at least contain {self.min_length} elements.")

        if self.max_length is not None and value > self.max_value:
            raise ValueError(f"{self.name} can not contain {self.max_length} elements.")

        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f'Item at index {index} is not a Point2D instance.')

        instance.__dict__[self.name] = list(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            if self.name not in instance.__dict__:
                instance.__dict__[self.name] = []
            return instance.__dict__[self.name]


class Polygon:

    vertices = Point2DSequence(min_length=3)

    def __init__(self, *vertices) -> None:
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Ca only append Point2D instances')

        max_length = type(self).vertices.max_length
        if max_length and len(self.vertices) >= max_length:
            raise ValueError(f'Vertices length is at max ({max_length}).')
        self.vertices.append(pt)
