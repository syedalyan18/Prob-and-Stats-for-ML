from scipy.stats import pearsonr,spearmanr
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])

r, _=pearsonr(x,y)
print("Pearson Correalation Coefficient : ",r)

r, _=spearmanr(x,y)
print("Spearman Correalation Coefficient : ",r)