import numpy as np

outcomes=np.array([1,2,3,4,5,6])
probability=np.array([1/6] *6)

expectations = np.sum(outcomes * probability)
print("Expectations (Mean) : ",expectations)

variance= np.sum((outcomes - expectations)**2 * probability)
std_dev=np.sqrt(variance)

print("Variance : ",variance)
print("Standard Deviation : ",std_dev)