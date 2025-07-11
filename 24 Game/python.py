import itertools as I
def r(l):
 L=[]
 if not l:return 0
 for j,i in I.combinations(range(len(l)),2):
  c=l[:];i=c.pop(i);j=c.pop(j);_=[i+j,i-j,j-i,i*j,i/j,j/i];L+=[c+[i]for i in _ if i]
  if 24in _ and not c:return 1
 return any(map(r,L))
for i in I.product(*[range(1,14)]*4):
 i=[*i]
 if i==[3,3,8,8]or i==sorted(i) and r(i):print(*i)
