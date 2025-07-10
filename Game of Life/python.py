import sys
r=sys.argv[t:=-1].split()
h,p='#.'
m=[[0]*32for _ in[0]*32]
for x in range(32):
 for y in range(32):
  for d,e in[(t,t),(t,c:=0),(t,1),(0,t),(0,1),(1,t),(1,0),(1,1)]:c+=0<=x+d<32and 0<=y+e<32and r[x+d][y+e]==h
  m[x][y]=[p,h][(r[x][y]==h)&(c in(2,3))or(r[x][y]==p)&(c==3)]
print("\n".join("".join(r)for r in m))
