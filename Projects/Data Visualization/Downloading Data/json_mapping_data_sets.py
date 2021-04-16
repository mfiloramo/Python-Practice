import json
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world import maps


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == "Vietnam":
            return 'vn'
    # If the country wasn't found, return None.
    return None


# # Load the data into a list.
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data
    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                print(f"{code}: {population}")
            else:
                print(f"ERROR: {country_name}")
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10_000_000:
        cc_pops_1[cc] = pop
    elif pop < 1_000_000_000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RS('#336699', base_style=LCS)

wm = maps.World(style=wm_style)
wm.title = "Populations of Countries in North America"
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
