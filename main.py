import random


class ParkingLot:
    """ Takes the total area of the parking lot and the area of a parking_spot and find total capacity of the
    parking lot """
    def __init__(self, total_area, spot_area):
        self.total_area = total_area
        self.spot_area = spot_area

    def parking_lot_arr(self):
        parking_lot = []
        arr_len = self.total_area // self.spot_area
        for i in range(arr_len):
            parking_lot.append(0)
        return parking_lot


# list of available spots
total_spots = ParkingLot(2000, 96).parking_lot_arr()


class Car:
    """ Create a car object with a 7digit license plate and park them to a random spot in the parking lot"""
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        # magic method to output the license plate on printing the object
        return f"License plate: {self.license_plate}"

    def park(self, parking_lot, spot):
        # function with a recursive call to park the current car in the spot if spot already occupied check new spot
        if parking_lot[spot] == 0:
            parking_lot[spot] = self.license_plate
            print(f"Car with license plate {self.license_plate} parked successfully in spot {spot}")
        else:
            print(f"Car with license plate {self.license_plate} parked cannot be parked in spot {spot}")
            if 0 in total_spots:  # checking if any empty spots in the parking lot
                for i in range(len(total_spots)):
                    if total_spots[i] == 0:
                        spot = i
                        return self.park(parking_lot, spot)  # recursive call of function
            else:
                print("Parking lot full")


def park_cars(cars_arr):
    for car in cars_arr:
        spot = random.randint(0, len(total_spots)-1)
        selected_car = Car(car)
        print(selected_car)
        selected_car.park(total_spots, spot)


# list of cars
cars = [1738452, 2731491, 3721984, 9732819, 4327981, 1131486, 1134653, 1232353, 8974565, 8977463, 9874532, 9084321,
        2365921, 5432617, 1453721]

# calling main method
park_cars(cars)

# output the parking lot to see all the occupied spots
print(total_spots)


# Sample Output
# License plate: 1738452
# Car with license plate 1738452 parked successfully in spot 16
# License plate: 2731491
# Car with license plate 2731491 parked successfully in spot 11
# License plate: 3721984
# Car with license plate 3721984 parked successfully in spot 15
# License plate: 9732819
# Car with license plate 9732819 parked cannot be parked in spot 15
# Car with license plate 9732819 parked successfully in spot 0
# License plate: 4327981
# Car with license plate 4327981 parked successfully in spot 13
# License plate: 1131486
# Car with license plate 1131486 parked successfully in spot 14
# License plate: 1134653
# Car with license plate 1134653 parked cannot be parked in spot 15
# Car with license plate 1134653 parked successfully in spot 1
# License plate: 1232353
# Car with license plate 1232353 parked successfully in spot 4
# License plate: 8974565
# Car with license plate 8974565 parked cannot be parked in spot 11
# Car with license plate 8974565 parked successfully in spot 2
# License plate: 8977463
# Car with license plate 8977463 parked successfully in spot 12
# License plate: 9874532
# Car with license plate 9874532 parked cannot be parked in spot 12
# Car with license plate 9874532 parked successfully in spot 3
# License plate: 9084321
# Car with license plate 9084321 parked cannot be parked in spot 11
# Car with license plate 9084321 parked successfully in spot 5
# License plate: 2365921
# Car with license plate 2365921 parked cannot be parked in spot 13
# Car with license plate 2365921 parked successfully in spot 6
# License plate: 5432617
# Car with license plate 5432617 parked cannot be parked in spot 0
# Car with license plate 5432617 parked successfully in spot 7
# License plate: 1453721
# Car with license plate 1453721 parked cannot be parked in spot 3
# Car with license plate 1453721 parked successfully in spot 8
# [9732819, 1134653, 8974565, 9874532, 1232353, 9084321, 2365921, 5432617, 1453721, 0, 0, 2731491, 8977463, 4327981,
# 1131486, 3721984, 1738452, 0, 0, 0]
