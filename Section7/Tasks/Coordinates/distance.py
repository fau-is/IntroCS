from math import sin, cos, atan2, sqrt

def calculate_distance(loc1, loc2):
    dlon = loc1.coordinate.longitude - loc2.coordinate.longitude
    dlat = loc1.coordinate.latitude - loc2.coordinate.latitude

    a = sin(dlat / 2) ** 2 + cos(loc1.coordinate.latitude) * cos(loc2.coordinate.latitude) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return 6373.0 * c