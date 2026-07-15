import matplotlib.pyplot as plt
from scipy.stats import uniform

outcomes=[1,2,3,4,5,6]
probability=[1/6]*6

plt.bar(outcomes,probability,color="blue",alpha=0.7)
plt.title("PMF of a Dice Roll")
plt.xlabel("Outcomes")
plt.ylabel("Probability")
plt.show()