
import pandas as pd

df = pd.read_csv("Books.csv")
print(df.head())
df.isnull().sum()
df.rename(columns={'User Rating': 'User_Rating'}, inplace=True)
df.info()
df.describe()
rating_df = df.groupby(['Author'], as_index=False).User_Rating.mean()
rating_df.rename(columns={'User_Rating': 'Average_User_Rating'}, inplace=True)
print(rating_df)
price_df = df.groupby(['Author'], as_index=False).Price.mean()
price_df.rename(columns={'Price': 'Average_Price'}, inplace=True)
print(price_df)
print("Maximum number of books are written by: ")
print(df['Author'].mode())
