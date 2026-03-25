#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input('N =', ))
M = int(input('M =', ))

class Fibonacci:
    def __init__(self, N, M):
        N = N
        M = M
        self.fib = [0, 1]
        while len(self.fib) < N:
            self.fib.append(self.fib[-2] + self.fib[-1])
            
    def fib1(self, N):
        return self.fib[N - 1]

    def fib2(self, N, M):
        fib_updated = []
        for i in range(len(self.fib) - 1):
            if self.fib[i] % M == 0:
                fib_updated.append(self.fib[i])
        return fib_updated

print(Fibonacci(N, M).fib1(N))
print(Fibonacci(N, M).fib2(N, M))


# In[ ]:




