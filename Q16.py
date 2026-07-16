import pandas as pd
from scipy.stats import ttest_ind

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df=pd.read_csv(url)

male_tips=df[df['sex'] == 'Male']['tip']
female_tips=df[df['sex'] == 'Female']['tip']

t_stat,p_value = ttest_ind(male_tips, female_tips)

print("T-Statistics : ",t_stat)
print("P-Value : ",p_value)

alpha=0.05

if p_value<=alpha:
    print("Reject all null hypothesis: Significant difference ")
else:
    print("Fail to reject all null hypothesis: No Significant difference ")