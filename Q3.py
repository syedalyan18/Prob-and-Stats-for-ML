import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

# outcomes=[1,2,3,4,5,6]
# probability=[1/6]*6

# plt.bar(outcomes,probability,color="blue",alpha=0.7)
# plt.title("PMF of a Dice Roll")
# plt.xlabel("Outcomes")
# plt.ylabel("Probability")
# plt.show()

x=np.linspace(0,1,100)
pdf=uniform.pdf(x,loc=0,scale=1)
plt.plot(x,pdf,color="orange")
plt.title("PDF of Uniform(0,1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()