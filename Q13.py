import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df=pd.read_csv(url)

del df["species"]

correlation_matrix=df.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Featuring Heatmap")
plt.show()