import sys
for k,a in enumerate(sys.argv[1:]):
 if k:print()
 H,W=map(int,a.split())
 g=[[' ']*W for _ in range(H)]
 x=y=0;dx=dy=1
 while 1:
  g[min(y,y+dy)][min(x,x+dx)]='\\' if dx*dy>0 else '/'
  x+=dx;y+=dy
  if x%W<1:dx=-dx
  if y%H<1:dy=-dy
  if x+y<1:break
 for r in g:print(''.join(r).rstrip())
