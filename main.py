from car_inventory import *

# ----------------------------
# Main Program
# ----------------------------
def main():
    cars = load_data()

    print("Welcome to the cars inventory system")

    while True:
        print("\nWhat would you like to do today?")
        print("-Add a car? enter 1")
        print("-Search for car 2")
        print("-Edit car info? enter 3")
        print("-Remove a car? enter 4")
        print("-Print the car list? enter 5")
        print("-Save the data to a file? enter 6")
        print("-Exit? enter 0.")

        choice = int(input(""))

        if choice == 1:
            add_car(cars)
        elif choice == 2:
            search_car(cars)
        elif choice == 3:
            edit_car(cars)
        elif choice == 4:
            remove_car(cars)
        elif choice == 5:
            print_cars(cars)
        elif choice == 6:
            save_data(cars)
        elif choice == 0:
            break

    # Program ends here. Data is saved whenever option 6 is chosen.


if __name__ == "__main__":
    main()