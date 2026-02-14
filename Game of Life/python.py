import sys
r=sys.argv[-1].split()
h='#'
m=[[0]*32for _ in[0]*32]
for x in range(32):
 for y in range(32):
  c=sum(32>x+d>=0<=y+e<32and r[x+d][y+e]==h for d in(-1,0,1)for e in(-1,0,1)if d|e)
  m[x][y]='.#'[c==3or c==2and r[x][y]==h]
print('\n'.join(map(''.join,m)))
