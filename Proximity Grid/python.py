import sys;S=''.join(filter(str.isalnum,map(chr,range(123))))+'-'
for A in sys.argv[1:]:
 G=[*A.replace(' ','\n')+'\n'*10];Q=[(i,0)for i in range(99)if'0'==G[i]]
 for i,v in Q:
  if v<=S.find(G[i]):G[i]=S[v];Q+=[(i+d,v+1)for d in(~9,~0,1,10)]
 print(*G[:-9],sep='')
