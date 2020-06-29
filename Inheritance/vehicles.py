v_list = []

class vehicle(object):
    ID = 1
    def __init__(self, type, passengers, brand):
        self.type = type
        self.passengers = passengers
        self.brand = brand
        self.id = vehicle.ID
        vehicle.ID += 1
        v_list.append(self)

    def get_id(self):
        return self.id

    def return_vehicle(self):
        return "ID: " + str(self.id) + "; " + "Type: " + str(self.type) + "; " + "Name: " + str(self.name) + "; " + "Brand: " + str(self.brand) + "; " + "Passengers: " + str(self.passengers)

    def br_path(self):
        if isinstance(self, car) or isinstance(self, truck):
            return ((self.speed_kmh / 10) * (self.speed_kmh / 10)) / 2
        else:
            return False

    def get_speed(self):
        if isinstance(self, car) or isinstance(self, truck):
            return self.speed_kmh
        else:
            return False

    def set_speed(self, speed):
        if isinstance(self, car) or isinstance(self, truck):
            self.speed_kmh = speed
        else:
            return False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class car(vehicle):
    def __init__(self, name, passengers, brand,  hp, max_velocity):
        super().__init__('car', passengers, brand)
        self.name = name
        self.hp = hp
        self.speed_kmh = max_velocity

class truck(vehicle):
    def __init__(self, name, passengers, brand, hp, max_velocity, max_load):
        super().__init__('truck', passengers, brand)
        self.name = name
        self.hp = hp
        self.speed_kmh = max_velocity
        self.max_load_kg = max_load

    def get_max_load(self):
        return self.max_load_kg
    def set_max_load(self, new_load):
        self.max_load_kg = new_load

class bike(vehicle):
    def __init__(self, name, passengers, brand, gears):
        super().__init__('bike', passengers, brand)
        self.name = name
        self.gears = gears

    def get_gear(self):
        return self.gears
    def set_gear(self, gears):
        self.gears = gears






