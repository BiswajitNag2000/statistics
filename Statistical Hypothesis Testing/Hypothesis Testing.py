import pandas as pd
from scipy.stats import ttest_1samp

df = pd.read_csv("Life Expectancy Data.csv")
data = df.dropna()
avg_world = data["Life expectancy "].mean()
afghani = data[data.Country == "Afghanistan"].sample(5, random_state=1)
print(df, data, avg_world, afghani)
alpha = 0.05
p = 1 - alpha / 2
df1 = 4
t_statistic, p_value = ttest_1samp(afghani["Life expectancy "], avg_world)
print('The t-statistic value is',t_statistic)
print('The p-value is',p_value)
if p_value < alpha: 
    print('We  reject the null hypothesis.\nThe average Life expectancy of afghanistan is not same as  average Life expectancy of world.')
else:
    print('We fail to reject  the null hypothesis.\nThe average Life expectancy of afghanistan is  same as average Life expectancy of world.')
