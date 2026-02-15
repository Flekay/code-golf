import sys
for a in sys.argv[1:]:
 H,W=map(int,a.split());g=[W*[c]for c in' '*H];x=y=0;u=v=c=1
 while c:g[y+v//2][x+u//2]='/\\'[u==v];x+=u;y+=v;u^=-2*(x%W<1);v^=-2*(y%H<1);c=x+y
 for r in g+['']:print(''.join(r).rstrip())