from itertools import*
r=lambda a:any(r([u]+C)if C else round(u,9)==24for A,B,*C in permutations(a)for u in(A+B,A-B,A*B,B and A/B))
for a in combinations_with_replacement(range(1,14),4):r(a)and print(*a)
