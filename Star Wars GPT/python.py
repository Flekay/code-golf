import sys
for a in sys.argv[1:]:
 t,*P=a.split('\n');w=t.split()
 for p in P:print(max(s:=[y for x,y in zip(w,w[1:])if x==p],key=s.count))
