import math
import time
n = 1000
res = 0
s = time.time()
for i in range(n):
    res += math.floor((i+1) * math.sqrt(2))
e = time.time()
print(res)
print(e-s)
