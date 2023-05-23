class Car:
    num_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.num_cars += 1

    @classmethod
    def get_num_cars(cls):
        return cls.num_cars

my_car = Car("Toyota", "Corolla", 2020)
print(Car.get_num_cars()) # output: 1

your_car = Car("Honda", "Civic", 2018)
print(Car.get_num_cars()) # output: 2
