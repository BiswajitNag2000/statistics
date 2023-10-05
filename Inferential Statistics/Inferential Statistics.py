import math

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine['feature_names'])
sample_size = 50
sample = df.sample(n=sample_size, random_state=100)
print(df, sample)
sample_mean = sample.alcohol.mean()
np.random.seed(1)

z_critical = stats.norm.ppf(q=0.95)

pop_stddev = sample.alcohol.std()

margin_of_error = z_critical * (pop_stddev / math.sqrt(sample_size))

confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)

print("Z-critical value:", z_critical, "Margin of Error:", margin_of_error, "Confidence Interval:", confidence_interval)
