from math import radians, sin, cos, atan2, sqrt

class Coordinate(object):
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    def return_coord(self):
        return self.latitude, self.longitude


class Location(object):
    location_list = list()
    
    def __init__(self, latitude, longitude, name):
        self.coordinate = Coordinate(latitude, longitude)
        self.name = name
        Location.location_list.append(self)

    def return_location(self):
        return self.name

    def return_distance(self, location):
        dlon = location.coordinate.longitude - self.coordinate.longitude
        dlat = location.coordinate.latitude - self.coordinate.latitude

        a = sin(dlat / 2)**2 + cos(location.coordinate.latitude) * cos(self.coordinate.latitude) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return 6373.0 * c


class City(Location):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude, name)
        self.population = population

    def return_pop(self):
        return self.population


if __name__ == "__main__":
    c1 = City(49.460983, 11.061859, "Nuremberg", 500000)
    c2 = City(48.137154, 11.576124, "Munich", 1300000)

    print(f"{round(c1.return_distance(c2), 2)}")