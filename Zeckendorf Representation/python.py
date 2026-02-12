import sys
for n in sys.argv[1:]:
 n=int(n);f=[1,2]
 while f[-1]<=n:f+=f[-1]+f[-2],
 r=[]
 for x in f[::-1]:
  if x<=n:r+=x,;n-=x
 print(' + '.join(map(str,r)))
