import sys
r=range(8)
R=-1,0,1
F=lambda x,y,I,J,z:8>x>-1<y<8!=(b:=a[y][x])>"."and(z,F(x+I,y+J,I,J,1))[b>"O"]
for a in sys.argv[1:]:a=a.split();*map(print,["".join((a[j][i],"!")[a[j][i]<"0"and any(F(i+I,j+J,I,J,0)for I in R for J in R if I|J)]for i in r)for j in r]+[""]),
