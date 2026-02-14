import sys
for a in sys.argv[1:]:
 s,t=a.split();d=range(len(t)+1)
 for c in s:d=[v:=-~d[0]]+[v:=-~min(v,q,p-(c==x))for x,p,q in zip(t,d,d[1:])]
 print(d[-1])