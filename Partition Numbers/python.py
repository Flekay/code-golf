p=[i:=1]+[0]*99
for _ in p:
 for j in range(i,100):p[j]+=p[j-i]
 i+=1
*map(print,p),
