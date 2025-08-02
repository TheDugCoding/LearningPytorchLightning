
class Battery():
    def __init__(self):
        self.battery_level = 100

class Car:
    # a function that is part of a class is called a method
    # init define the attributes of a class
    def __init__(self, make, model, year):
        #these are attributes
        self.make = make
        self.model = model
        self.year = year
        #we can also set attributes (even classes) without passing the parameter
        self.speed = 0
        self.battery = Battery()

    def drive(self):
        print(f'I\'m driving my {self.model} at {self.speed} km/h')

    def change_speed(self, speed):

        if speed > 0:
            print('accelerating')
            self.speed += speed
        else:
            print('deaccelerating')
            self.speed += speed

#this is inheritance, we take info from the parent class, we also take all the methods
class ElectricCar(Car):
    #call the
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery.battery_level = 80

    def drive(self):
        if self.speed > 0:
            self.battery.battery_level -= 10
        print(f'I\'m driving my {self.model} at {self.speed} km/h, battery level is {self.battery.battery_level}')


if __name__ == "__main__":
    #new_car is called an instance of a class
    new_car = Car('Ford', 'Falcon', 2020)
    #you can access attributes and functions by using .
    new_car.drive()
    new_car.change_speed(100)
    new_car.drive()
    new_car.change_speed(-50)
    new_car.drive()
    electric_car = ElectricCar('Tesla', 'Tesla', 2020)
    electric_car.drive()
    electric_car.drive()
    electric_car.change_speed(100)
    electric_car.drive()