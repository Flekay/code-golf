import sys
m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for r in sys.argv[1:]:v=[m[c]for c in r];print(sum(v)-2*sum(a for a,b in zip(v,v[1:])if a<b))
