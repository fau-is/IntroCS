![fau-logo](https://introcs.is.rw.fau.de/img/logos/ReWi_logo.png)

## Complete vehicles.py

**Before tackling this task, make sure you have you have watched MITs Lecture on object oriented
programming**

{% next %}

## Program Specifications

This problem aims at improving your command of working with python classes and the inheritance
structure. You will be required to create classes and subclasses. Hand in hand with this you will 
need to define certain methods in order to be able to work with all the classes that are defined.

The issue at hand is to build a hierarchical class inheritance structure for vehicles. The parent- or superclass will
be called "vehicle". You then need to define the data attributes and procedural attributes. Furthermore, 
the superclass vehicle has 3 child- or subclasses namely car, truck and bike. In turn these classes again 
require some data attributes as well as procedural attributes.

Once you have completed all the tasks that are described for each class you then need to run 
**sup.py** which will then access the vehicles.py file and work with the classes you have just defined.

**You can have a look a the "sup.py" file. However, do not change or add anything in this file.**

We will now continue and start describing what attributes each class requires. Afterwards we will
have a look at all the methods that need to be introduced.

**IMPORTANT: Note that you need to give every attribute and method in your program the same
name that we specify in the following. Otherwise the sup.py caller file will not work. Furthermore,
we have numbered the attributes of each class. This is the order they need to be written 
into the constructor of each class. Please pay attention to this!**

{% next "Class Attributes"%}

## Superclass vehicle - Attributes

This is your parent class. The constructor should take 4 positional arguments.

~~~
self = the variable that refers to any instance of the class
type = the type of the vehicle i.e. car, truck or bike
passengers = the amount of passengers a vehicle can hold
brand = the brand of the vehicle
~~~
Further, the superclass should include an attribute 'ID' which is initially set to 1. However,
with every instance that is created of class vehicle the ID should increase by 1.
~~~
v1 = vehicle(type, passengers, brand)
v2 = vehicle(type, passengers, brand)
print(v1.get_id)
print(v2.get_id)

Output:
1
2
~~~
Additionally, after every time a instance of class vehicle is created this instance should
be automatically appended to the predefined list called "v_list"

## Subclass car - Attributes

This is your first subclass. The constructor should take 6 positional arguments. 2 of which
need to be passed into the superclass.
~~~
1. self = the variable that refers to any instance of the subclass and superclass
2. name = name of the car i.e. Golf
3. passengers = needs to be passed to superclass
4. brand = also needs to be passed to superclass
5. hp = horsepower of car
6. max_speed_kmh = the fastest the car can go in kph
~~~
now you will notice that there is no attribute 'type'. This is not a argument that needs to be
passed into a certain class as the class car itself is the type. I.e. you will need to find a way
to add the type to the superclass without taking it in as a positional argument.

## Subclass truck - Attributes

This is your second subclass. The constructor should take 7 positional arguments. 2 of which
need to be passed into the superclass.

~~~
1. self = the variable that refers to any instance of the subclass and superclass
2. name = name of the truck i.e. Raptor
3. passengers = needs to be passed to superclass
4. brand = also needs to be passed to superclass
5. hp = horsepower of car
6. speed_kmh = the fastest the car can go in kph
7. max_load_kg = the maximum weight a truck can load in kg
~~~
Again you will notice that there is no attribute 'type'. This is for the same reasons as 
described in car class.

## Subclass bike - Attributes

This is your final subclass. The constructor should 5 positional arguments. 2 of which need
to be passed into the superclass.

~~~
1. self = = the variable that refers to any instance of the subclass and superclass
2. name = name of the bike i.e. VanMoof
3. passengers = needs to be passed to superclass
4. brand = needs to be passed to superclass
5. gears = the amount of gears a bike has. 
~~~

And once more there is no attribute 'type'. for the same reasons as given above.

{% next "Class Methods"%}

## Class Methods

We will now go over some methods that you are required to define for each class.

## Methods vehicle

**get_id()** = This method should return the ID of the class instance. Note that it should
not print the ID! The ID needs to be returned.

**return_vehicle()** = This method returns a string which includes the base information of each 
instance of the class! Make sure that the string being returned is in the correct format specified below.
~~~
Example:
 
ID: 1; Type: car; Name: Golf VII; Brand: Volkswagen; Passengers: 5

~~~

**br_path()** = this method calculates the emergency break path of your vehicle when going 
at top speed. The formula is the following. 
~~~
emergency brake path = (max_speed_kmh / 10 * max_speed_kmh / 10) / 2
~~~
This method should return the value calculated with the formula given above. Furthermore,
you need to pay attention. This formula only works for instances of classes that possess
the attribute 'max_speed_kmh'. As the class bike does not have this attribute you need to check
first before calculating that the instance you are using the formula on is indeed of type
car or truck. 'isinstance()' is a useful method here. If the instance is of class bike the 
method should return false.

**get_speed()** = returns the maximum speed of a vehicle. Again check whether the associated
instance is actually able to return their max speed. 

**set_speed()** = sets the max speed a vehicle can go. Again check whether the associated
instance actually possesses a 'max_speed_kmh' attribute. 

**get_name** = returns the name of a vehicle regardless of type.

**set_name** = sets a name for a vehicle regardless of type.

## Methods car

There is no method that needs to be specified for the subclass car

## Methods truck

**get_max_load()** = returns the 'max_load_kg' attribute of the class instance

**set_max_load()** = sets the 'max_load_kg' attribute of the class instance

## Methods bike

**get_gear()** = returns the 'gears' attribute of the class

**set_gear()** = sets the 'gears' attribute of the class

{% next "Summary" %}

The task at hand is not tricky to do. However, it is a lot of details that you will need
to take into account. Please do this task the way we defined it. Especially when naming your 
classes, attributes and methods.

As mentioned earlier the goal of the task at hand is to apply your newly learned knowledge on 
OOP and Inheritance based programming as well as class Hierarchies.

**Don't forget. In order to run your program you need to run the 'sup.py' file. Nevertheless,
if you want to check for certain things in your 'vehicles.py' file feel free to use print functions etc.
within the file and run it. However, please remove them before submitting or checking**

If you require any guidance let us know.

**Have fun coding!**

{% next "Library Talk" %}

## Libraries

**Note** that for this task you will not require any libraries.

{% next "Check & Submit" %}

## Check 

You can check your code using the following check50 command:

~~~
$check50 fau-is/IntroCS/Pset7/Inheritance --local
~~~

## Submit

You can submit your code to us via the following submit50 command:

~~~
submit50 fau-is/introcs/Pset7/Inheritance
~~~
