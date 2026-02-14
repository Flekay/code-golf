import sys
F=lambda a,x,y,X,Y,z:0if not(8>x>-1<y<8)or(b:=a[y][x])=="."else z if b=="O"else F(a,x+X,y+Y,X,Y,1)
for a in sys.argv[1:]:a=a.split();r=range(8);R=range(-1,2);*map(print,["".join("!"if(A:=a[j][i])=="."and any(F(a,i+I,j+J,I,J,0)for I in R for J in R if I or J)else A for i in r)for j in r]+[""]),
