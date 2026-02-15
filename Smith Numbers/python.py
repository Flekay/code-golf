i=3
while i<1e4:
 j=i=i+1;s=sum(b'%d'%i)
 for k in range(2,i):
  while j%k<1:j//=k;s-=sum(b'%d'%k)
 s%48or print(i)
