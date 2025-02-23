import numpy as np
import scipy.stats as stats




def z_scorez(sample_proportion,poblational_proportion,n):

# Cálculo del Z-score

print(sample_proportion)
print(poblational_proportion)
print(n)

z_score = (sample_proportion - poblational_proportion) / np.sqrt((poblational_proportion * (1 - poblational_proportion)) / n)

return (z_score)
