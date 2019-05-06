import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day': [1,2,3,4,5,6],
             'Visitors': [43,53,34,45,64,34],
             'Bounce_Rate': [65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)

#print(df)
#print(df.head())
#print(df.tail())
print(df.tail(2))   # prints 2 rolls from the bottom

print(df.set_index('Day'))
#df.set_index('Day', inplace=True) or equate the function to
#  a variable(df2) then print to set the index permanently

print(df.head())

# t reference a specific column
print(df['Bounce_Rate'])
#or
print(df.Visitors)

print(df[['Bounce_Rate', 'Visitors']])      # to refernce two columns
print(df.Visitors.tolist())
print(np.array(df[['Bounce_Rate', 'Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))

print(df2)