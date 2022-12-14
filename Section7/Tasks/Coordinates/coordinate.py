from math import radians

def main():
    c1 = City(49.460983, 11.061859, "Nuremberg", 500000)
    c2 = City(48.137154, 11.576124, "Munich", 1300000)

    print(f"{round(c1.return_distance(c2), 2)}")


if __name__ == "__main__":
    main()

