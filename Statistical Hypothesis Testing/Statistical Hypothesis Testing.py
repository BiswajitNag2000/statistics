import math
total_mean = 5
sample_mean = 2
standard_deviation = 3
sample_size = 50
significant_interval = 1.96  
error_rate = standard_deviation/(math.sqrt(sample_size))
UCV = int(total_mean + (significant_interval*error_rate))
LCV = int(total_mean - (significant_interval*error_rate))
print(UCV,LCV)
if UCV < sample_mean or sample_mean < LCV:
    print(" we are rejecting null hypothesis and accepting alternate hypothesis")
else:
    print("we are accepting null hyporhesis")