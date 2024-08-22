from abc import ABC, abstractmethod

class Car:

    def start_engine(self):

        raise NotImplementedError("Subclass must implement this method")

class Honda(Car):

    def start_engine(self):

        return "The Honda engine has started."

class BMW(Car):

    def start_engine(self):

        return "The BMW engine has started."

def start_car_engine(car):

    print(car.start_engine())

honda_car = Honda()

bmw_car = BMW()

start_car_engine(honda_car)

start_car_engine(bmw_car)