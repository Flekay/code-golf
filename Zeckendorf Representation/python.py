import sys
for n in sys.argv[1:]:
 n=int(n);f=1,2
 while f[-1]<n:f+=f[-1]+f[-2],
 print(' + '.join([str(x)for x in f[::-1]if x<=n and((n:=n-x)or 1)]))
