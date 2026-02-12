import sys
for r in sys.argv[1:]:v=[5**((p:='IVXLCDM'.find(c))%2)*10**(p//2)for c in r];print(sum(v)-2*sum(a for a,b in zip(v,v[1:])if a<b))
