import sys
from string import*
S=digits+ascii_uppercase+ascii_letters+"-"
for A in sys.argv[1:]:
 def I(x,y,v):
  if-1<x<9and-1<y<9and(t:=A[x][y])in S and v<=S.index(t):A[x][y]=S[v];[I(x+d%3-1,y+d//3-1,v+1)for d in(1,3,5,7)]
 A=[[*_]for _ in A.split()];[I(i,j,0)for i in range(9)for j in range(9)if A[i][j]=="0"];*map(print,[*map(''.join,A),'']),
