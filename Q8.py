import numpy as np
import pandas as pd
from scipy.stats import norm

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df=pd.read_csv(url)

sample=df["sepal_length"].sample(30, random_state=42)

mean = sample.mean()
std_dev = sample.std()
n = len(sample)

z_value = norm.ppf(0.975)
margin_of_error = z_value * (std_dev / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)
print("Sample Mean : ",mean)
print("Standard Deviation : ",std_dev)
print("95% Confidence Interval ; ",ci)