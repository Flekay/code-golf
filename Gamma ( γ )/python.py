P=t=S=10**1005;T=h=L=k=0
while t:k+=1;L+=P//k>>k;t=(t<<20)//k//k;h+=P//k;S+=t;T+=t*h
print(f'0.{T//S-10*L}'[:-5])