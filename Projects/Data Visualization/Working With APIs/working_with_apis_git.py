import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def get_conf_code(url):
    """Returns a confirmation code to a user-inputted URL (designed for tests_apis_git.py)."""
    r = requests.get(url)
    return f"Status code: {r.status_code}"

def get_repo_dicts(url):
    """Returns a repository count to a user-inputted URL (designed for tests_apis_git.py)."""
    r = requests.get(url)
    response_dict = r.json()
    return f"Total repositories: {response_dict['total_count']}"


# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Number of items: {len(repo_dicts)}")

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Javascript Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('javascript-repos.svg')

# print(f"Repositories returned: {len(repo_dicts)}")
# print("\nSelected information about each repository:\n")
#     print(f"Name: {repo_dict['name']}")
#     print(f"Owner: {repo_dict['owner']['login']}")
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     print(f"Repository: {repo_dict['html_url']}")
#     print(f"Created: {repo_dict['created_at']}")
#     print(f"Updated: {repo_dict['updated_at']}")
#     print(f"Description: {repo_dict['description']}\n")

# Process results.
# print(response_dict.keys())
