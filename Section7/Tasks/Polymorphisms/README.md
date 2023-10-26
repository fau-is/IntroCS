---
files: [method_overlapping.py]
window: [terminal]
---
# Polymorphism

## Dynamic Typing
Python utilises dynamic typing (Duck typing).
That means we do not need to declare a variable type during runtime.
We can use that to our advantage in regards of flexibility, reusability and recyclability.

In the file action.py create three classes:
* Controller,
* CreateHelloPy
* CreateHelloC.
None of them needs a constructor ;)

In the classes CreateHelloC/Py implement a method “run” which writes a “Hello World” program in the respective language in a file called hello.c/hello.py

In Controller, add a method “execute” which takes one argument obj. The method should call obj.run().

## Method Overloading
Method overloading refers to functions with the same name, but different parameters.
It usually results in different functionalities.

In method_overloading.py, Create a function sum that can sum up at leas two and up to four numbers at the same time.

## Operator overloading
In items.py, implement a class Item(), which represents an item on a payment receipt.

Item should have three attributes; the name of an item, the quantity and the price per piece.
Additionally, item has one method _price()_ which multiplies the quantity with the price per piece to calculate the total price.

In a main function, construct two items and sum them up using the ‘+’ operator.

What happens?

Assuming we want to receive the total price as a result.
Therefore you need to override the _add_(self, other) function.

## Method Overriding
Open items.py, and implement three subclasses of Item:
* FoodItem => A food item is taxed with 7%.
* NonFoodItem => A non-food item is taxed 16%.
* SpecialOfferItem => “50% off”-offer; it is taxed 19%.

Override the method price() in each of the sub_classes to take care of the above mentioned specifications.
