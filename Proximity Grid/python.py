import sys;j=range(9)
for a in sys.argv[1:]:
 g=a.split();d=[[-1]*9for _ in[0]*9]
 for r,c in(q:=[(r,c)for r in j for c in j if g[r][c]=='0']):d[r][c]=0
 while q:(x,y),*q=q;[exec('d[n][m]=d[x][y]+1;q+=[(n,m)]')for w,z in[(0,1),(1,0),(0,-1),(-1,0)]if 0<=(n:=x+w)<9and 0<=(m:=y+z)<9and g[n][m]=='-'and d[n][m]<0]
 *map(print,[''.join(g[r][c]if g[r][c]!='-'else'-'if(z:=d[r][c])<0else chr(z+(48if z<10else 55if z<36else 61))for c in j)for r in j]+['']),
