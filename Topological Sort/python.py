import sys
for a in sys.argv[1:]:
 w=a.split();r=[]
 while S:={*w}-{*r}:r+=min(S-{b for a,b in zip(*[iter(w)]*2)if{a}&S})
 print(*r)
