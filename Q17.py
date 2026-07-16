import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df=pd.read_csv(url)

x=df["total_bill"].values.reshape(-1,1)
y=df["tip"].values

model=LinearRegression()
model.fit(x,y)

slope=model.coef_[0]
intercept=model.intercept_
r_squared=model.score(x,y)

print("Slope : ",slope)
print("Intercept : ",intercept)
print("R-Squared : ",r_squared)

sns.scatterplot(x=df['total_bill'],y=df['tip'],color="blue")
plt.plot(df['total_bill'],model.predict(x),color="red",label="Regression Line")
plt.title("Total bill vs Tip")
plt.legend()
plt.show()