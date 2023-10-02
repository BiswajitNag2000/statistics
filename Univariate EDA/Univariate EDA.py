import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("cereal.csv")
mfg = {'A': 'American Home Food Products', 'G': 'General Mills', 'K': 'Kelloggs',
       'N': 'Nabisco', 'P': 'Post', 'Q': 'Quaker Oats', 'R': 'Ralston Purina'}
df2 = df['mfr'] = df['mfr'].replace(mfg)
top_5_rating = df.sort_values(by='rating', ascending=False).reset_index(drop=True).head()
print(top_5_rating)
print(df.describe())
print(df.info())
print(df2)
df.groupby('mfr')['rating'].mean().plot.bar()
plt.ylabel('Customer Ratings')
plt.xlabel('Manufacturer')
plt.title('Manufacturers with Highest Customer Ratings', fontsize=20)
plt.show()
df3 = df['mfr'].value_counts().to_frame().reset_index()
plt.pie(df3['mfr'], labels=df3['index'])
plt.title('Manufacturers which are largest Producers', fontsize=20)
plt.show()
