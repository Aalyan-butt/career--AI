import numpy as np     
from scipy import stats 

# marks = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])


# print(np.mean(marks))
# print("Median", np.median(marks))
# print("Variance", np.var(marks))
# print("Standard Deviation", np.std(marks))

# print ("Mode", stats.mode(marks))

# modulus


# dice = np.arange(1,7)
# print("Even", np.mean(dice%2==0))

#  Suppose 5 % of emails are spam and 95% are safe.
# If an email is flagged as spam, there is a 90% chance
# that it is actually spam, and a 10% chance that it is safe.

spam = 0.05
safe = 1 - spam

flag_spam = 0.9
flag_safe = 0.1

print(spam * flag_spam)

print(safe * flag_safe)

print(flag_spam +flag_safe)