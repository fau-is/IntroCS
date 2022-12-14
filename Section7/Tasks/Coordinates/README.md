# Coordinates
## Coordinate Class
In coordinate.py, create a class _Coordinate_.
Coordinate's constructor requires two parameters _latitude_ and _longitude_.
Each parameter is provided as a string and should be converted to the type math.radians.
Additionally, implement a method return_coord which returns both properties.

## Location
In the same file, create the class _Location_ that has _two attributes_: _coordinate_ and _name_.
Location's constructor requires three parameters _latitude_, _longitude_, and _name_.
In the constructor, you must create a Coordinate object which is stored in the attribute _coordinate_ and the name should likewise be stored in the attribute _name_.
Furthermore, you should create a return_location method that returns the name of the location. An array locations which is a class variable of Location stores every Location that is created.

## City
Now create another class City that is a subclass of location.
It should take 4 parameters: latitude, longitude, name and population.
Pass latitude and longitude as well as name to the parent classes constructor.
Population is an attribute specific to the subclass City.
Lastly create a method that returns the population of a City.

## Distance
Create a method for your location parent class called return_distance.
This method should return the distance between two instances of class location.
Don’t worry about the calculation we provide it for you on the next slide in the solutions.
However, the method should take self as an argument and another location called loc1.
Before we calculate we need to first check whether loc1 is in actual fact an instance of class location and whether both the coordinate properties of self and loc1 are instances of class coordinates. After checking you can insert the calculations we provide you with..