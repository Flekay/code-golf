i=3
while i<1e4:
 i+=1;j=i;s=0
 for k in range(2,i):
  while j%k<1:j//=k;s+=sum(map(int,str(k)))
 s-sum(map(int,str(i)))or print(i)
