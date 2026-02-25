import sys
r=sys.argv[1].split()+[''];R=range(32)
for x in R:print(''.join('.#'[2<sum(r[x+d].count('#',~1%-~y,y+2)for d in(-1,0,1))<4+(r[x][y]<'.')]for y in R))
