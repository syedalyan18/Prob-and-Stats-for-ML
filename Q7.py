import numpy as np
from scipy.stats import norm

data = np.random.normal(loc=50,scale=10,size=100)

mean = np.mean(data)
std_dev = np.std(data, ddof=1)
n = len(data)

z_value = norm.ppf(0.975)
margin_of_error = z_value * (std_dev / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)
print("Sample Mean : ",mean)
print("Standard Deviation : ",std_dev)
print("95% Confidence Interval ; ",ci)
