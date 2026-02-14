m,*p=0,
for n in range(250):m-=n-2*n*(n>m or m-n in p);p+=[m];print(m)
