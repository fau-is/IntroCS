---
files: [coordinate.py]
window: [terminal]
---
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
Now create another class _City_ that is a subclass of _Location_. It should take 4 parameters: latitude, longitude, name and population. Pass latitude and longitude as well as name to the parent classes constructor Population is an attribute specific to the subclass City.
Lastly create a getter method for the population attribute of a City.

## Distance
Import the function from distance.py and try to calculate the distance between two of your coordinates.
Does it work? If it works you have implemented your classes correctly.
