#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4.6 session quiz
import numpy as np
from matplotlib import pyplot as plt
import scipy as sy

a = float(input("a ="))
b = float(input("b ="))

def f(x):
    y = x
    return y
ans = sy.integrate.quad(f, a, b)

x = "x^$"
print(f'The integral of {f(x)} between {a} and {b} is {ans[0]}')

