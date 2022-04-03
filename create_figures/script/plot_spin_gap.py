import numpy as np
import matplotlib.pyplot as plt

N = 5

up = (0.0814, 0.2932, 0.2355, 0.3386, 0.3078)
down = (0.0522, 0.0523, 0.0343, 0.0000, 0.0495)
ind = np.arange(N)
width = 0.35

#fig = plt.subplots(figsize =(10, 7))
p1 = plt.bar(ind, up, width, bottom = down)
p2 = plt.bar(ind, down, width)

plt.ylabel('Contribution to the band gap')
plt.title('Structure')
plt.xticks(ind, ('A', 'B', 'C', 'D', 'E'))
#plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Up', 'Down'))

plt.show()
