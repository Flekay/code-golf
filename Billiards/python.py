import sys
for a in sys.argv[1:]:
 H,W=map(int,a.split());g=[W*[c]for c in' '*-~H];x=y=0;u=v=c=1
 while c:g[y+v-1][x+u-1]='/\\'[u==v];x+=2*u-1;y+=2*v-1;u^=x%W<1;v^=y%H<1;c=x+y
 for r in g:print(''.join(r).rstrip())