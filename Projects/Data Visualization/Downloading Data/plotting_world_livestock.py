import json
import csv
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world import maps


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country"""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == "Vietnam":
            return 'vn'
    # If the country wasn't found, return None.
    return None


filename = "world_livestock_data.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# Build a dictionary of population data
    cc_livestock_numbers = {}
    for row in reader:
        try:
            country_name = row[0]
            livestock = float(row[5])
            code = get_country_code(country_name)
        except ValueError:
            print("Missing Data")
        except IndexError:
            print("Missing Data")
        else:
            print(f"{code}: {livestock}")
            cc_livestock_numbers[code] = livestock

# Group the countries into 3 livestock levels.
cc_lives_1, cc_lives_2, cc_lives_3 = {}, {}, {}
for cc, lives in cc_livestock_numbers.items():
    if lives < 50:
        cc_lives_1[cc] = lives
    elif lives < 100:
        cc_lives_2[cc] = lives
    else:
        cc_lives_3[cc] = lives

wm_style = RS('#336699', base_style=LCS)

wm = maps.World(style=wm_style)
wm.title = "World Livestock Output, 1961"
wm.add('0-50l', cc_lives_1)
wm.add('50-100l', cc_lives_2)
wm.add('100+l', cc_lives_3)

wm.render_to_file('world_livestock_1961.svg')
