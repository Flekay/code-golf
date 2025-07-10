import math
f=[]
for d in range(1,51):
 for n in range(d+1):
  if math.gcd(n,d)<2:f+=(n,d),
f.sort(key=lambda z:z[0]/z[1])
for x in f:print(f'{x[0]}/{x[1]}')
