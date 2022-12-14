# Decorators

## Sytax
Decorators are always written atop the function or class they should modify.

```Python
@decorator
def some_method:

@class_decorator
class SomeClass:
```

## Static Methods
Static methods do not work on instances, but are still encapsulated in a class. Note the missing of ‘self’. Therefore, the context of a method remains clear.
Static methods do not know anything about the actual class, similar to a function.
A static method is declared with a decorator:
_@staticmethod_

## Class Methods
Class methods operate on class scope. Note the first parameter cls. The function can access class information but not instance information. This is particularly useful when using the classmethod to create instances of the class in a different way as the constructor.
A class method is declared with a decorator:
_@classmethod_

## Property
A property is a 


