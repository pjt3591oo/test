import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(10000)

print(data)
plt.hist(data, bins=50)
plt.show()