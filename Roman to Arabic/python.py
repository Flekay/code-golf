import sys
for s in sys.argv[1:]:
 t=0
 for r in s:n=10**'IXCMVLD'.find(r)%9995;t+=n-2*t%n
 print(t)
