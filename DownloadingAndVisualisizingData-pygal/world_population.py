import json

from world_countries_codes import get_country_codes


# Load the data into a list

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
# Print 2010 population from list
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # population data has to be in the correct format for PyGal
        population = int(float(pop_dict['Value']))
        code = get_country_codes(country_name)
        if code:
            print(code + ':' + str(population)+ ':' + country_name)
        else:
            print('ERROR - ' + country_name)
