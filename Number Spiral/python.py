m='',;s=100
while s:e=s;s-=len(m);m=range(s,e),*zip(*m[::-1])
for r in m:print(('%3d'*10%(*r,))[1:])
