i=3
while i<1e4:
 i+=1;j=i;s=""
 for k in range(2,i):
  while j%k<1:j//=k;s+=str(k)
 if sum(map(int,str(i)))==sum(map(int,s)):print(i)
