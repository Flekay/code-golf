p=[1]+[i:=0]*99
for _ in p:
 for j in range(i:=i+1,100):p[j]+=p[j-i]
*map(print,p),
