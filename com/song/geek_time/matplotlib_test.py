import matplotlib.pyplot as plt

# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
# plt.plot(x,np.sin(x))
# plt.show()

# plt.figure(1, dpi=50)
# for i in range(1, 5):
#     plt.plot(x, np.sin(x / i))
# plt.show()


plt.figure(1,dpi=50)
data = [1,1,1,2,2,2,3,3,4,5,5,6,4]
plt.hist(data)
plt.show()