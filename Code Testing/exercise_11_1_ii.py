from exercise_11_1 import get_formatted_location

print("Enter 'q' anytime to quit!\n")

while True:
    city = input("Name your city: ")
    if city == 'q':
        break
    country = input("Which country is that city located? ")
    if country == 'q':
        break

    formatted_location = get_formatted_location(city,country)
    print("Your location is - " + formatted_location + ".")