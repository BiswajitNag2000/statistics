import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("winequality-red.csv")
print(df.head())
np.random.seed(11)
sample_7_and_above = data[data['quality'].isin([7, 8])].sample(10)[['alcohol']].reset_index().drop(columns=['index'])

m = np.mean(sample_7_and_above["alcohol"])
print("The mean of the sample is: ", m)
sd = np.std(sample_7_and_above["alcohol"])
print(data, sample_7_and_above, ("The standard deviation of the sample is: ", sd))

sns.distplot(sample_7_and_above["alcohol"], hist=False)
title = "mean of sample 1 = " + str(m) + ", standard deviation ofsample 1 = " + str(sd)
plt.title(title)
plt.show()
n = 10
s = sd
standard_error = s / np.sqrt(n)
print('Standard Error is:', standard_error)
