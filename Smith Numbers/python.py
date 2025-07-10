for n in range(9986):
 r,k,l,f=2,str(n),'',0
 while n>1:
  while n%r<1:l+=str(r);f+=1;n//=r
  r+=1
 if(f>1and sum(map(int,l))==sum(map(int,k))):print(k)
