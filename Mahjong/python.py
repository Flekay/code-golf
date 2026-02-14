import itertools as I,sys
for a in sys.argv[1:]:
 A=sorted(ord(_)-126983for _ in a);L=[(_,)*3for _ in A if A.count(_)>2]+[(_,_+1,_+2)for _ in A if _>=0and _%9<7and _+1in A and _+2in A]
 if{*A}=={*range(-7,1),8,9,17,18,26}or all(a.count(_)==2for _ in a)or any(sorted(sum(_,()))==A for _ in I.product(L,L,L,L,[(_,)*2for _ in A])):print(a)
