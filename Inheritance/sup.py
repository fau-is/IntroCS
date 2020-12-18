import vehicles

car = vehicles.car("Golf VII", 5, "Volkswagen", 105, 195)
truck = vehicles.truck("F-150 Raptor", 5, "Ford", 450, 230, 1500)
bike = vehicles.bike("X3", 1, "VanMoof", 4)

for items in vehicles.vehicle.v_list:
    print(items.type, " ", end="")
print()

print(vehicles.car.return_vehicle(car))
print(vehicles.truck.return_vehicle(truck))
print(vehicles.bike.return_vehicle(bike))

print(vehicles.car.br_path(car))

vehicles.truck.set_speed(truck, 240)
print(vehicles.truck.get_speed(truck))
if vehicles.bike.set_speed(bike, 50) == False:
    print("Bike rejected successfully")

print(vehicles.truck.get_max_load(truck))
