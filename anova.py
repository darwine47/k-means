import numpy
import numpy as np

p1 = [21, 20, 16]
p2 = [16, 18, 11]
p3 = [23, 31, 24]
p = p1+p2+p3

n1 = len(p1)
n2 = len(p2)
n3 = len(p3)
N = n1 + n2 + n3

T1 = sum(p1)
T2 = sum(p2)
T3 = sum(p3)
T = T1+T2+T3

x1 = np.average(p1)
x2 = np.average(p2)
x3 = np.average(p3)
mean = (x1+x2+x3)/3

print("N = {}; ".format(N), "T = {}; ".format(T), "Moyenne = {}; ".format(mean))

sceT = (sum(map(lambda i : i*i, p)))-((T*T)/N)
t1 = T1**2
t2 = T2**2
t3 = T3**2
sceA = (t1/n1)+(t2/n2)+(t3/n3)-((T*T)/N)
sceR = sceT - sceA
print("SCEt = {} ".format(sceT),"SCEa = {}".format(sceA),"SCEr = {}".format(sceR))
