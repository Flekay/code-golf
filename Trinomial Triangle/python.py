r=1,
for _ in range(20):print(*r);r=*map(sum,zip((0,0)+r,[0,*r,0],r+(0,0))),
