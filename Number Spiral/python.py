n=10;a=[[-1]*n for _ in[0]*n];x=y=d=i=0;p=0,1,0,-1,0
while i<n*n:a[x][y]=i;d=d if 0<=x+p[d]<n>y+p[d+1]>=0>a[x+p[d]][y+p[d+1]]else(d+1)%4;x+=p[d];y+=p[d+1];i+=1
for r in a:print(*map('{:2}'.format,r))
