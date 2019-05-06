import requests

import pygal

from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

url = 'https://api.github.com/search/repositories?q=language:JavaScript&sort=stars'
r = requests.get(url)
response_dict = r.json()
print('Status code:', r.status_code)

repo_dicts = response_dict['items']

names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    description = repo_dict['description']
    if not description:
        description = 'No description provided'

    plot_dict = {'value': repo_dict['stargazers_count'], 'label':
        repo_dict['description'], 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 20
my_style.major_label_font_size = 16

my_config = pygal.Config()
my_config.show_y_guides = False
my_config.x_label_rotation = 45
my_config.truncate_label = 15
my_config.show_legend = False
my_config.width = 500

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Javascript on Github'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('exercise_17_1_java.svg')