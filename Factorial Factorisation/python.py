n,*f=1000,
for p in[i for i in range(2,n+1)if all(i%j for j in range(2,int(i**.5)+1))]:
 c,r=0,p
 while r<n:c+=n//r;r*=p
 if c:f+=f"{p}"+"^%d"%c*(c>1),
print("*".join(f))
