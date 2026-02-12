S=lambda n:sum(map(int,str(n)))
i=3
while i<1e4:
 i+=1;j=i;s=0
 for k in range(2,i):
  while j%k<1:j//=k;s+=S(k)
 s-S(i)or print(i)
