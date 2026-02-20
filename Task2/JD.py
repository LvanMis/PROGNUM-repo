#!/usr/bin/env python
# coding: utf-8

# In[2]:


Y = float(input("Year:" ))
Y2 = float(input("Year of birth:" ))

M = float(input("Month:" ))
M2 = float(input("Month of birth:" ))

D = float(input("Day:" ))
D2 = float(input("Day of birth:" ))

Age = 367 * Y - 7 * (Y + (M + 9)/12)/4 - 3 * ((Y + (M - 9)/7)/100 + 1)/4 + (M * 275)/9 + D + 1721029 - 0.5 - (367 * Y2 - 7 * (Y2 + (M2 + 9)/12)/4 - 3 * ((Y2 + (M2 - 9)/7)/100 + 1)/4 + (M2 * 275)/9 + D2 + 1721029 - 0.5)

print(Age)


# In[ ]:




