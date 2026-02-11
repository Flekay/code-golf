import sys
for a in sys.argv[1:]:
 L=a.split('\n');w=L[0].split()
 for p in L[1:13]:
  d={};f={}
  for j in range(len(w)-1):
   if w[j]==p:
    n=w[j+1];d[n]=d.get(n,0)+1
    if n not in f:f[n]=j
  print(min(d,key=lambda x:(-d[x],f[x])))
