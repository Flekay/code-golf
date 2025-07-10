z=lambda n:0if[i for i in range(2,int(n**.5+1))if n%i<1]else 1
n,*f=1000,
for p in[i for i in range(2,n+1)if z(i)]:
 c,r=0,p
 while r<n:c+=n//r;r*=p
 if c:f+=[[f"{p}^{c}"],[f"{p}"]][c<2]
print("*".join(f))
