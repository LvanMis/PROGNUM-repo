#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

a = 7
b = -3
c = -8
print(f"a is {a}, b is {b} and c is {c}")

if a == 0:
    if b != 0:
        x = -c/b
        print(f"There is one solution for x = {x}")
    else:
        print("There is only a solution for x = infinity")
else:
    D = b**2 - 4 * a * c
    if D == 0:
        x = -b/(2*a)
        print(f"There is one solution for x = {x}")
    elif D > 0:
        x1 = (-b + (D)**0.5)/(2*a)
        x2 = (-b - (D)**0.5)/(2*a)
        print(f"There are two solutions for x_1 = {x1} and x_2 = {x2}")
    else:
        print("There are no real solutions")


# In[ ]:




