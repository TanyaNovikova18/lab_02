import math
from math import cos, sin
N=3
c=0
s=0
k=1
for i in range(1, N+1):
    c+=math.cos(i)
    s+=math.sin(i)
    k*=c/s
print(k)
