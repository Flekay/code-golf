from itertools import*
for n in range(4,9):
 for v in permutations(c:=range(1,n+1)):
  if n==len({i+v[i-1]for i in c})==len({i-v[i-1]for i in c}):print(*v,sep='')
