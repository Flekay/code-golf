import itertools as I,sys
for a in sys.argv[1:]:
 A=sorted(ord(_)%64for _ in a)
 if{*A}=={*range(8),15,16,24,25,33}or{*map(a.count,a)}=={2}or A in(sorted(sum(x,()))for x in I.product(*4*[[(_,)*3for _ in A if A.count(_)>2]+[(_,_+1,_+2)for _ in A if _>6and(_-7)%9<7and{_+1,_+2}<={*A}]],zip(A,A))):print(a)
