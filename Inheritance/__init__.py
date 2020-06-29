import check50
import check50.py

p0 = "car  truck  bike  "
p1 = "ID: 1; Type: car; Name: Golf VII; Brand: Volkswagen; Passengers: 5"
p2 = "ID: 2; Type: truck; Name: F-150 Raptor; Brand: Ford; Passengers: 5"
p3 = "ID: 3; Type: bike; Name: X3; Brand: VanMoof; Passengers: 1"
p4 = "190"
p5 = "240"
p6 = "Bike rejected successfully"
p7 = "1500"


@check50.check()
def exists_sup():
    """sup.py"""
    check50.exists("sup.py")

@check50.check(exists_sup)
def exists_vehicles():
    """vehicles.py"""
    check50.exists("vehicles.py")

@check50.check(exists_sup)
def compiles():
    """sup.py runs"""
    check50.run("python3 sup.py")

@check50.check(compiles)
def check():
    """sup.py does what it is supposed to do"""
    check50.run("python3 sup.py").stdout(p0).stdout(p1).stdout(p2).stdout(p3).stdout(p4).stdout(p5).stdout(p6).stdout(p7)