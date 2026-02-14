import sys
for a in sys.argv[1:]:
 H,W=map(int,a.split())
 g=[[' ']*W for _ in[0]*H]
 x=y=0;dx=dy=1
 while 1:
  g[y+dy//2][x+dx//2]='/\\'[dx*dy>0]
  x+=dx;y+=dy
  if x%W<1:dx=-dx
  if y%H<1:dy=-dy
  if x+y<1:break
 for r in g:print(''.join(r).rstrip())
 print()
