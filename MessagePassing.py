class Car:

    def __init__(self, brand):

        self.brand = brand

    def start_engine(self):

        print(f"The {self.brand} engine has started.")

class Driver:

    def __init__(self, name):

        self.name = name

    def drive(self, car):

        print(f"{self.name} is driving the car.")

        car.start_engine()

car = Car("Toyota")

driver = Driver("John")

driver.drive(car)
