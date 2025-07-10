x=y=e=0
t=[[-1]*10for _ in[0]*10]
d=[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(100):
 t[x][y]=i;a,b=d[e];w,z=x+a,y+b
 if not(0<=w<10>z>=0>t[w][z]):a,b=d[e:=(e+1)%4];w,z=x+a,y+b
 x,y=w,z
for r in t:print(*[f"{n:2}"for n in r])
