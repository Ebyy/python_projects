import requests

import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def get_response():
    """Make an API call and return the response"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    return r

def get_repo_dicts(response):
    """Return set of dicts with the most repositories"""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_names_plot_dicts(repo_dicts):
    """Return plot value list of names and plot_dicts"""
    names, plot_dicts = [], []

    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        description = repo_dict['description']
        if not description:
            description = 'Description not provided.'

        plot_dict = {'value': repo_dict['stargazers_count'],
                     'xlink': repo_dict['html_url'],
                     'label': description}
        plot_dicts.append(plot_dict)
    return names, plot_dicts

def make_visualization(names, plot_dicts):
    """Make visualization"""
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.show_legend = False
    my_config.show_y_guides = False
    my_config.x_label_rotation = 45
    my_config.truncate_label = 15
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos_exercise.svg')

r = get_response()
repo_dicts = get_repo_dicts(r)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)