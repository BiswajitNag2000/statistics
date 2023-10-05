import math

total_mean = 50000
sample_mean = 48000
standard_deviation = 15
sample_size = 100
significant_interval = 1.96
error_rate = standard_deviation / (math.sqrt(sample_size))
UCV = int(total_mean + (significant_interval * error_rate))
LCV = int(total_mean - (significant_interval * error_rate))
if UCV < sample_mean or sample_mean < LCV:
  print(" we are rejecting null hypothesis and accepting alternate hypothesis")
else:
  print("we are accepting null hyporhesis")
