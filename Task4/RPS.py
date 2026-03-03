#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# Don't do anything other than the options
x =input("Rock, paper, scissors?", )
options = ["R", "P", "S"]

# Give a computer output. We need to make sure there is no cheating though
output = np.random.randint(0, 3, 1)
comp_choice = options[output[0]]
print(comp_choice)

# All possibilities for outcomes
if x == comp_choice:
    print("Tie")
elif x == "R":
    if comp_choice == "P":
        print("I win")
    else:
        print("You win")
elif x == "P":
    if comp_choice == "R":
        print("You win")
    else:
        print("I win")
else:
    if comp_choice == "R":
        print("I win")
    else:
        print("You win")

