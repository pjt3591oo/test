import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100000)

plt.hist(data, bins=100)
plt.show()