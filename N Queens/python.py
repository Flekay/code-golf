from itertools import*
r=range
[print(n*'%d'%v)for n in r(4,9)for v in permutations(r(1,n+1))if all(abs(v[i]-v[j])-i+j for i in r(n)for j in r(i))]