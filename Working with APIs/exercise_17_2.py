import requests
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS
from operator import itemgetter

#analysing article submissions made to hacker news
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)
submission_ids = r.json()

submission_dicts = []

for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/'
           + str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_list = submission_r.json()
    print(submission_r.status_code)

    submission_dict = {'title': response_list['title'],
                       'link': 'http://news.ycombinator.com/item?id=' +
                       str(submission_id),
                       'comments': response_list.get('descendants', 0)}
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])

    plot_dict = {'value': submission_dict['comments'],
                 'xlink': submission_dict['link'],
                 'label': submission_dict['title']}
    plot_dicts.append(plot_dict)

# Make visualisation.
my_style = LS('#336699', base_style=LCS)
my_style.title_font_size = 24
my_style.major_label_font_size = 16
my_style.label_font_size = 14

my_config = pygal.Config()
my_config.show_y_guides = False
my_config.show_legend = False
my_config.x_label_rotation = 45
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Active Discussions on HackerNews'
chart.x_labels = titles
chart.add('', plot_dicts)

chart.render_to_file('exercise_17_2_hn_submissions.svg')
