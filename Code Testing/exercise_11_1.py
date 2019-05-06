def get_formatted_location(city,country,population=0):
    """Format input to give City,Country."""
    formatted_location = city.title() + ', ' + country.title()
    if population:
        formatted_location += ' - population ' + str(population)
    return formatted_location