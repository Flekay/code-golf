z=lambda n:all(n%i for i in range(2,int(n**.5+1)))
n,*f=1000,
for p in[i for i in range(2,n+1)if z(i)]:
 c,r=0,p
 while r<n:c+=n//r;r*=p
 if c:f+=[f"{p}"+f"^{c}"*(c>1)]
print("*".join(f))
