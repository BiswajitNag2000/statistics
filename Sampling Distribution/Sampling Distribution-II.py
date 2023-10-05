import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("winequality-red.csv")
np.random.seed(11)
seed = np.arange(0, 9)

x_bar = []
std_dev = []

for s in seed:
    np.random.seed(s)
    sample_7_and_above = data[data['quality'].isin([7, 8])].sample(10)[['alcohol']].reset_index().drop(
        columns=['index'])
    x_bar.append(np.mean(sample_7_and_above["alcohol"]))
    std_dev.append(np.std(sample_7_and_above["alcohol"]))

samples = pd.DataFrame(columns=["Sample Means (X_bar)", "Sample Standard Deviation (s)"],
                       data=list(zip(x_bar, std_dev)))
print(samples)
sns.distplot(samples["Sample Means (X_bar)"])
plt.title("Distribution of the sample means")
plt.show()
standard_error = np.array(samples['Sample Means (X_bar)']).std()
print('The Standard Error is:', standard_error)
