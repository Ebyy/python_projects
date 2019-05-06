import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)
response_list = r.json()

repo_dicts = response_list['items']

# Prepare lists of values to be plotted.
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'], 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

# Make visualisation.
my_style = LS('#336666', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legends=False,
                  show_y_guides=False, width=1000)
chart.title = 'Most-Starred C Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('exercise_17_1_C.svg')
