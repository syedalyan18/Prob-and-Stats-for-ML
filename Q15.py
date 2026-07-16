import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df=pd.read_csv(url)

print(df.info())
print(df.describe())
del df["sex"]
del df["day"]
del df["smoker"]
del df["time"]

# Visualization Distributions
sns.histplot(df["total_bill"],kde=True)
plt.title("Distribution of total bill")
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()