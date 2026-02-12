a=[[-1]*10for _ in[0]*10];x=y=d=i=0;p=0,1,0,-1
while i<100:a[x][y]=i;d+=(0<=x+p[d]<10>y+p[d-3]>=0>a[x+p[d]][y+p[d-3]])<1;d%=4;x+=p[d];y+=p[d-3];i+=1
for r in a:print(*map('{:2}'.format,r))
