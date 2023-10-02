import matplotlib.pyplot as plt
import pandas as pd
import scipy
import seaborn as sns
from scipy import stats

df = pd.read_csv("exam.csv")
print(df, ('Number of rows:', df.shape[0]), ('Number of columns:', df.shape[1]), df.describe())
cols = ["math score", "reading score", "writing score"]
fig, ax = plt.subplots(1, 3, figsize=[15, 5])
for variable, subplot in zip(cols, ax.flatten()):
    plot = sns.distplot(x=df[variable], ax=subplot, hist=False)
    plot.set_xlabel(variable, fontsize=15)
    plt.tight_layout()
    plt.show()

for a in cols:
    print("\n")
    print('Mean of ', a, ':', scipy.mean(df[a]))
    print('Standard Deviation of ', a, ':', scipy.std(df[a]))
    for a in cols:
        skewness = stats.skew(df[a])
        print("\n")
        print('The Skewness of the', a, ' distribution:', skewness)

        kurtosis = stats.kurtosis(df[a])
        print('The Kurtosis of the', a, ' distribution:', kurtosis)
        z_scores = stats.zscore(df[a], axis=0)
        print("\n")
        print("z_score of", a, ":\n", z_scores)
        ig, ax = plt.subplots(1, 3, figsize=[20, 5])
        for variable, subplot in zip(cols, ax.flatten()):
            plot = sns.distplot(stats.zscore(df[variable], axis=0), ax=subplot, hist=False)
            plot.set_xlabel(variable, fontsize=15)
        plt.tight_layout()
        plt.show()
