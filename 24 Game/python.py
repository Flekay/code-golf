from itertools import*
r=lambda a:any(round(u,9)==24and c==[]or u and r(c+[u])for x,y in combinations(a,2)for c in[[*a]]if c.remove(x)==c.remove(y)for u in(x+y,x-y,y-x,x*y,x/y,y/x))
for a in combinations_with_replacement(range(1,14),4):r(a)and print(*a)
