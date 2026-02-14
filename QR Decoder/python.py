import sys
Q=sys.argv[1].split("\n");S=-1;j=20;q=""
for s,e in [(20,8),(9,21)]*2+[(20,-1),(0,21)]+[(12,8),(9,13)]*2:
 for i in range(s,e,S):
  if i==6:continue
  p=(i+j)%2;q+=str((Q[i][j]>' ')^1^p)+str((Q[i][j-1]>' ')^p)
 S*=-1;j-=3if j==8else 2
for i in range(12,148,8):print(chr(int(q[i:i+8],2)),end="")
