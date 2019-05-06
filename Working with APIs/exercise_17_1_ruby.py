import requests

import pygal

from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
r = requests.get(url)
print(r.status_code)
response_list = r.json()

repo_dicts = response_list['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    description = repo_dict['description']
    if not description:
        description = 'No description provided'

    plot_dict = {'value': repo_dict['stargazers_count'], 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#336699', base_style=LCS)
my_style.title_font_size = 24
my_style.major_label_font_size = 18
my_style.label_font_size = 14

ruby_config = pygal.Config()
ruby_config.show_legend = False
ruby_config.show_y_guides = False
ruby_config.width = 1000
ruby_config.truncate_label = 15
ruby_config.x_label_rotation = 45

chart_ruby = pygal.Bar(ruby_config, style=my_style)
chart_ruby.title = 'Most-Starred Ruby Projects on GitHub'
chart_ruby.x_labels = names
chart_ruby.add('', plot_dicts)

chart_ruby.render_to_file('exercise_17_1_ruby.svg')
