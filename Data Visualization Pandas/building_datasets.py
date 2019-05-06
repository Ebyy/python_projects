import quandl
import pandas as pd
import html

api_key = open('qandl_api.txt', 'r').read()

df = quandl.get('FMAC/HPI_AK', authotoken=api_key)

#print(df.head())

fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#print(fifty_states) - this is a list

#this is a dataframe
#print(fifty_states[0])

# this is a column
#print(fifty_states[0][0])

#for abbv in fifty_states[0][0]:
    #print('FMAC/HPI_' + str(abbv))

print(fifty_states[0][0][1:])