import pandas as pd

df = pd.read_csv('Housing_data_Texas.csv')

df.set_index('Date', inplace=True)

df.to_csv('newcsv2.csv')        # to save the csvfile

df = pd.read_csv('newcsv2.csv')
print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('newcsv3.csv', header=False)    # This retains just the data without headers
# to read the headers back in

df = pd.read_csv('newcsv3.csv', names=['Date','Austin_HPI'], index_col=0)

print(df.head())

# the data can also be save to another format

df.to_html('example.html')
