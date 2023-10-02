import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("cereal.csv")
mfg = {'A': 'American Home Food Products', 'G': 'General Mills', 'K': 'Kel lo ggs',
       'N': 'Nabisco', 'P': 'Post', 'Q': 'Quaker Oats', 'R': 'Ra ls ton Purina'}
df2= df['mfr'] = df['mfr'].replace(mfg)
rating_between_50_to_100 = df[(df['rating'] >50.0) & (df['rating']<100.0)]
df3= df.iloc[:, :-4]
corr_mat = df3.corr()
cov_mat = df3.cov()
print(df, df2, rating_between_50_to_100.head(), corr_mat, cov_mat)
sns.lmplot(x="protein", y="calories", hue="mfr", data=df)
plt.show()
plt.subplots(figsize=(12, 9))
sns.heatmap(corr_mat, annot=True)
plt.title('Correlation between the Nutritional values: ', fontsize=20)
plt.show()
plt.subplots(figsize=(12, 9))
sns.heatmap(cov_mat, annot=True)
plt.title('Covariance between the Nutritional values: ', fontsize=20)
plt.show()
