#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
from matplotlib import pyplot as plt
import scipy

x = np.linspace(-10, 10, 200)

def gauss(x):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

A = float(input("A ="))
x0 = float(input("x0 ="))
sigma = float(input("sigma ="))
z0 = float(input("z0 ="))
a = float(input("a ="))
b = float(input("b ="))

print('integration area =', scipy.integrate.quad(gauss, a, b))
plt.plot(x, gauss(x))
plt.fill_between(x, gauss(x), 4,
                 where = (x >= a) & (x <= b),
                 alpha = 0.5, label = f'area: {scipy.integrate.quad(gauss, a, b)[0]}')

plt.legend()
plt.show()


# In[ ]:




