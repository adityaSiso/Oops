"""
What is an object?
    - Consider it as a container
        + contains data --> state --> attributes
        + contains functionality --> behaviour --> methods

Class: It is a template to create the objects.
Instance: Objects created of the class is an instance.
"""


# ------------------------------------------------------------------------------
"""
Instance of a class is of type *CLASS*
Class of the instance is of type *TYPE*
"""
class MyClass:
    pass

# MyClass.__name__ -> 'MyClass' (state)
# MyClass() -> obj of MyClass which is callable (behaviour)

instance = MyClass()

# type(MyClass) -> type (metaclasses)
# type(instance) -> __main__.MyClass


# ------------------------------------------------------------------------------
"""
Class attributes not instance attributes.
"""
class Program:
    language = 'python'
    version = 'v3.10.12'

# With the __name__ method the class now also contains the class attributes
# language and version.

print(Program.language) # python
print(Program.version)  # v3.10.12

# The dot-notation is similar to calling getattr.
# getattr(object, attr_name, default).

getattr(Program, 'language', 'N/A') # python
getattr(Program, 'venv', 'N/A')     # N/A

# State of all the attributes of MyClass get populated in a dictionary.
MyClass.__dict__ # 'mappingproxy' which is a dict with key as attribute name
# in string and value as the attribute value. This dict can only be mutated
# using the setattr method.
"""
Note: __dict__ does not holds all the attributes.
"""
MyClass.venv = '/opt/....'
setattr(MyClass, 'venv', '/opt/....')

delattr(MyClass, 'venv') # Both will delete the class attributes and they will
del MyClass.venv         # Also be removed from the state of the MyClass object.


# ------------------------------------------------------------------------------
"""
Callable class

Note: The instance of a class and the class itself has different namespaces.
      This can be checked by using the __dict__ method on both.
Every instance has its own namespace.
"""


# ------------------------------------------------------------------------------
"""Data attributes of class and instance."""

class BackendEmployee:
    language = 'python'
    version = '3.10'

e1 = BackendEmployee()

# Example of different namespaces...
BackendEmployee.__dict__ # {'language': 'python', 'version': '3.10', ....}
e1.__dict__              # {}

# But...
e1.language # python
# Why is that because python first check the instance namespace then the class
# namespace returns it from there.

e1.language = 'java' # This is similar to setattr
e1.__dict__ # {'language': 'java'}
e1.language # java

e2 = BackendEmployee()
e2.__dict__ # {} (type of this is dict)
BackendEmployee.__dict__ # {'language': 'python', 'version': '3.10', ....}
# (type of this is mappingproxy)


# ------------------------------------------------------------------------------
"""Functions attributes of class and Instance."""

class BackendEmployee:
    language = 'Java'
    version = '15.0.1'

    def fun(obj):
        pass

BackendEmployee.fun     # Function of MyClass
e1 = BackendEmployee()
e1.fun                  # Bound method of MyClass to the e1 object.
# e1.fun.__self__ Represents the e1 object
# e1.fun__func__ Represents the bound method.
e1.fun() # = MyClass.fun(e1)

# Method = instatnce + function.

"""Note: A function will only bound to an object if it defined in the class."""
BackendEmployee.is_admin = lambda self: f'Yes {self} is admin.'
BackendEmployee.__dict__ # We will be able to the is_admin as method in
                         # mappingproxy.
e1.is_admin # Bound method

e1.is_senior = lambda *args: f'Yes {args} is senior.' # This be a method not a
                                                      # Bound method to e1 obj.


# ------------------------------------------------------------------------------
"""Initializing class Instance"""

class BackendEmployee:

    def __init__(self): # Object is already created by __new__ method.
        print(f'Hello from {self}.')

e1 = BackendEmployee() # __new__ -> __init__
# BackendEmployee() = BackendEmployee.__init__(e1)

# We can customize the instance creation process by overriding __new__ method.


# ------------------------------------------------------------------------------

