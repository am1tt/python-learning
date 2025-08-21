

class Vehicle:
    def show_type(self): 
        print("Vehicle : used for transpot")


class Car(Vehicle): 
    def car_feature(self): 
        print("Car : Has 4 wheels and AC")

class Electric: 
    def battery_info(self): 
        print("Electric : Runs of battery")

class ElectricCar(Car,Electric):
    def features(self): 
        print( "Electriccar : eco friendly and silient")


ecar = ElectricCar()

ecar.show_type()