from itertools import*
def r(a):
 for i,j in combinations(range(len(a)),2):
  b=a[:];x=b.pop(j);y=b.pop(i);t=[x+y,x-y,y-x,x*y,x/y,y/x]
  if 24 in t and not b or any(u and r(b+[u])for u in t):return 1
for a in product(range(1,14),repeat=4):
 if a==(3,3,8,8)or a==tuple(sorted(a))and r(list(a)):print(*a)
