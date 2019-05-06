from car_class_module import Car, Electric_Car

#Multiple classes have been imported from that module and are available for use.

my_beetle = Car('volkswagen','beetle',2005)
print(my_beetle.get_descriptive_name())

my_tesla = Electric_Car('tesla','model s',2017)
print(my_tesla.get_descriptive_name())