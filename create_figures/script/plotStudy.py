import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()

structures = ['fe2si', 'fesi2', 'crsi2', 'mnsi1.75']
permutations = [10, 50, 5, 20]

plt.barh(structures, permutations)
plt.xlabel("Number of composistions/permutations")
plt.show()
