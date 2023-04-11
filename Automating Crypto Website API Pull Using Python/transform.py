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

#it is series now not a df
type(df4)
#change it back to df
df5 = df4.to_frame(name='values')

# how many rows we have, I need it for creating index for df6
df5.count()

index = pd.Index(range(90))

#to insert index
df6 = df5.reset_index()
df6

#rename for better understanding
df7 = df6.rename(columns ={'level_1': 'percent_change'})
df7

df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df7

import seaborn as sns
import matplotlib.pyplot as plt

sns.catplot(x='percent_change', y='values', hue='name', data = df7, kind='point')
plt.show()

df10 = df_1988[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Bitcoin'")
df10

sns.set_theme(style='darkgrid')
sns.lineplot(x='timestamp', y='quote.USD.price', data= df10)
plt.show()
