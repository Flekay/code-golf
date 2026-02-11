import sys
r=sys.argv[-1].split()
h,p='#.'
m=[[0]*32for _ in[0]*32]
for x in range(32):
 for y in range(32):
  c=sum(32>x+d>=0<=y+e<32and r[x+d][y+e]==h for d in(-1,0,1)for e in(-1,0,1)if d|e)
  m[x][y]=[p,h][(r[x][y]==h)&(c in(2,3))or(r[x][y]==p)&(c==3)]
print("\n".join("".join(r)for r in m))
