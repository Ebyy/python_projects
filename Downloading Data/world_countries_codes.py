from pygal_maps_world.i18n import COUNTRIES


def get_country_codes(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for country_code, name in COUNTRIES.items():
        if name == country_name:
            return country_code
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Moldova':
        return 'md'
    elif country_name == 'Macedonia, FYR':
        return 'mk'
    elif country_name == 'Libya':
        return 'ly'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kp'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Hong Kong SAR, China':
        return 'hk'
    elif country_name == 'Gambia, The':
        return 'gm'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Bolivia':
        return 'bo'
    elif country_name == 'Congo, Rep.':
        return 'cg'
    elif country_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif country_name == 'Tanzania':
        return 'tz'
    # If the country wasn't found, return None
    return None
