import requests

import pygal

from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store results in a readable format in a variable
response_dict = r.json()
print("Total Repositories:", response_dict['total_count'])


repo_dicts = response_dict['items']

# Build lists of values to be plotted
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title ='Most-Starred Python Projects on GitHub'
chart.x_labels=names

chart.add('', stars)
chart.render_to_file('python_repos2.svg')