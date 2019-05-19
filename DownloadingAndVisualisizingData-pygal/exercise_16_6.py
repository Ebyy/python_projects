import json

import pygal

from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from pygal.maps.world import World

from world_countries_codes import get_country_codes

# Load the data into a list
filename = 'global_gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Create dictionary to store values
cc_gdps = {}
for gdp_value in gdp_data:
    if gdp_value['Year'] == '2014':
        country_name = gdp_value['Country Name']
        gdp = int(float(gdp_value['Value']))
        code = get_country_codes(country_name)
        if code:
            cc_gdps[code] = gdp

# Group data into 3 levels
cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 5000000000:
        cc_gdps_1[cc] = round(gdp/1000000000)
    elif gdp < 50000000000:
        cc_gdps_2[cc] = round(gdp/1000000000)
    else:
        cc_gdps_3[cc] = round(gdp/1000000000)

print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))


wm_style = RS('#336699', base_style=LCS)

wm = World(style=wm_style)

wm.title = "Global GDP in 2014, by Country"
wm.add('0-5bn', cc_gdps_1)
wm.add('5bn-50bn', cc_gdps_2)
wm.add('>50bn', cc_gdps_3)

wm.render_to_file('world_gdp.svg')
