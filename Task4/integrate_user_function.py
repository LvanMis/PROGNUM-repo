#!/usr/bin/env python
# coding: utf-8

# In[55]:


from numpy import sin, cos, exp, pi
import numpy as np
import scipy as sy

# user input
try:
    a1 = input("a =")
    a = float(a1)
    b1 =input("b =")
    b = float(b1)
    x = np.linspace(a, b, 10000)
except:
    if b1 or a1  == "":
        print("please enter a number")

finally:
    try:  
        user_input = input('function =')
        y = sum(eval(user_input))

        # monte carlo integrater
        def s(y):
            return (b - a)/10000 * y
        print('using monte carlo integration with 10000 samples:', s(y))

    except:
        print("please enter a function using x and proper python syntax")    


# In[ ]:





# In[ ]:




