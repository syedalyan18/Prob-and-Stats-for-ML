import numpy as np

rolls=np.random.randint(1,7,size=10000)
p_even= np.sum(rolls % 2 == 0) / len(rolls)
p_greater= np.sum(rolls > 4) / len(rolls)

print("Prob (even) : ",p_even)
print("Prob (greater than 4) : ",p_greater)