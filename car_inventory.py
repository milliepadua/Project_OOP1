"""
Names: Vitor Peixoto, Millie Padua, Qusai Alotaiki
Date: December 2025
Project: Car Inventory Program
Description:
This program is a Car Inventory System that allows the user to add, search,
edit, remove, print, and save car records. Each car is stored as an object in
a list and contains an ID, name, make, body type, year, and value. When the
program starts, it automatically loads any existing data from data.txt, and
when requested, it saves updated data back to the same file. The program guides
the user through a menu-driven interface that matches the provided test plan.
All processing includes proper data-type conversion, formatted output, and
persistent storage so the inventory can be reused between runs.
"""

# ----------------------------
# Car Class
# ----------------------------
class Car:
    def __init__(self, cid, name, make, body, year, value):
        self.cid = cid
        self.name = name
        self.make = make
        self.body = body
        self.year = int(year)
        self.value = float(value)

    def __str__(self):
        # Use tabs so columns line up nicely in console
        return f"{self.cid}\t{self.name}\t{self.make}\t{self.body}\t{self.year}\t{self.value:.1f}"


# ----------------------------
# Load Data From File
# ----------------------------
def load_data():
    cars = []
    try:
        with open("data.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                cid, name, make, body, year, value = line.split(",")
                cars.append(Car(int(cid), name, make, body, int(year), float(value)))
    except FileNotFoundError:
        # No existing file yet, start with empty inventory
        pass
    return cars


# ----------------------------
# Save Data To File
# ----------------------------
def save_data(cars):
    with open("data.txt", "w") as f:
        for c in cars:
            f.write(f"{c.cid},{c.name},{c.make},{c.body},{c.year},{c.value}\n")
    print("Data saved to local file successfully!")


# ----------------------------
# Add Car
# ----------------------------
def add_car(cars):
    while True:
        print("\nEnter id of the car, followed by the car's information.")
        cid = int(input("Id:\n"))
        name = input("name:\n")
        make = input("make:\n")
        body = input("Body:\n")
        year = int(input("year:\n"))
        value = float(input("value:\n"))

        # First, check for duplicate ID
        duplicate_id = any(c.cid == cid for c in cars)

        # Second, check if the exact same car is already in the inventory
        duplicate_car = any(
            c.name == name and c.make == make and c.body == body
            and c.year == year and c.value == value
            for c in cars
        )

        if duplicate_id:
            print("Incorrect Id. Id already exist in the system.")
        elif duplicate_car:
            print("The car is already in the inventory. No action is required..")
        else:
            cars.append(Car(cid, name, make, body, year, value))
            print("car is added to the inventory.")
            print(cars[-1])

        more = input("Do you want to add more cars? y(yes)/n(no)\n")
        if more.lower() != "y":
            return


# ----------------------------
# Search Car
# ----------------------------
def search_car(cars):
    while True:
        print("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
        choice = int(input(""))

        if choice == -1:
            return

        elif choice == 1:
            cid = int(input("Please Enter the id of the car:\n"))
            found = next((c for c in cars if c.cid == cid), None)
            if found:
                print("Car found ", found)
            else:
                print("Car not found")

        elif choice == 2:
            name = input("Please Enter the name of the car:\n")
            found = next((c for c in cars if c.name == name), None)
            if found:
                print("Car found ", found)
            else:
                print("Car not found")


# ----------------------------
# Edit Car
# ----------------------------
def edit_car(cars):
    while True:
        print("Enter the id of the car. Enter -1 to return to the previous menu")
        cid = int(input(""))
        if cid == -1:
            return

        target = next((c for c in cars if c.cid == cid), None)
        if not target:
            # If id not found, just ask again (test plan doesn't show an error)
            continue

        name = input("Name:\n")
        make = input("make:\n")
        body = input("Body:\n")
        year = int(input("year:\n"))
        value = float(input("value:\n"))

        target.name = name
        target.make = make
        target.body = body
        target.year = year
        target.value = value

        print(f"Car's new info is {target}")


# ----------------------------
# Remove Car
# ----------------------------
def remove_car(cars):
    while True:
        print("Enter id of the car that you want to remove from the inventory.")
        cid = int(input("id:\n"))

        found = next((c for c in cars if c.cid == cid), None)

        if found:
            cars.remove(found)
            print("car removed")
        else:
            print("Car not found")

        more = input("Do you want to remove more cars? y(yes)/n(no) ")
        if more.lower() != "y":
            return


# ----------------------------
# Print Car List
# ----------------------------
def print_cars(cars):
    for c in cars:
        print(c)


