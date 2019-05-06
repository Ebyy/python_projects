import car_class_module as car

#the entire module has beeen imported

my_truck = car.Car('toyota','hilux',2013)
print(my_truck.get_descriptive_name())

#the 'as' can be removed and the code adjusted to yeild the same result.
#also from module_name import * can be used to import all the classes in
#that module but it isn't recommended because confusion can ensue as a result
#of names already in use in the program being repeated in the imported classes