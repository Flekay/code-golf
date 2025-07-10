import sys
for arg in sys.argv[1:]:
 x,y=arg.split();m=len(x)+1;d=[[*range(n:=len(y)+1)]]+[[i] for i in range(1,m)]
 for j in range(1,n):
  for i in range(1,m):d[i].insert(j,min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+int(x[i-1]!=y[j-1])))
 print(d[-1][-1])
