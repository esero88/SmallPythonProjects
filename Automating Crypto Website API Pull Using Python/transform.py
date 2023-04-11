import pandas as pd

df_1988 = pd.read_csv(r'C:\Users\Eser\Documents\Python Scripts - VSCode\API.csv')

#to make numbers make readable
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#group by the percent changes with respect to time
df3 = df_1988.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3
print(df3)

#to make it like pivot table
df4 = df3.stack()
df4
print(df4)