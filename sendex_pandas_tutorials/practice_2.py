import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)
# print(df.head())
# print(df.tail())

# print(df.set_index('Day'))
# df = df.set_index('Day')
print(df.head())
# OR more directly
# df.set_index('Day', inplace=True)

# to reference a column
print(df.Visitors)
# or
print(df['Bounce_Rate'])
# or for two columns
print(df[['Bounce_Rate', 'Visitors']])

# print(df.Visitors.tolist())
# print(df[['Bounce_Rate', 'Visitors']].tolist())...wont work because it is an array

# for arrays
print(np.array(df[['Bounce_Rate', 'Visitors']]))

# or you can make it a 2nd dataframe and use it

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)

df.set_index('Date', inplace=True)