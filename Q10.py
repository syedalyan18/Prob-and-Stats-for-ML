from scipy.stats import ttest_1samp,ttest_ind,ttest_rel

# One sample test
data=[12,14,15,16,17]
population_mean=15
t_stat,p_value=ttest_1samp(data,population_mean)

print("One sample test : ",t_stat,p_value)

# Two sample test
group1=[12,14,15,16,17]
group2=[11,13,14,15,16]
t_stat,p_value=ttest_ind(group1,group2)

print("Two sample test : ",t_stat,p_value)

# Paired test
pre_test=[12,14,15,16,17]
post_test=[13,14,16,17,18]
t_stat,p_value=ttest_rel(pre_test,post_test)

print("Paired test : ",t_stat,p_value)