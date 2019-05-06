from car_class_module import Car

my_car = Car('toyota','corolla',2016)
print (my_car.get_descriptive_name())

my_car.odometer_reading = 50
my_car.read_odometer()