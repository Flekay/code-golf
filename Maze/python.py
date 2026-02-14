import sys
m=sys.argv[1].split('\n');s,e=[(r,c)for r in range(51)for c in range(51)if m[r][c]in'SE']
q,v=[(*s,[])],{s}
while q:
 (r,c,p),*q=q
 if(r,c)==e:
  for x,y in p[1:]:m[x]=m[x][:y]+'.'+m[x][y+1:]
  *map(print,m),
 for a,b in(-1,0),(1,0),(0,-1),(0,1):
  if 0<(x:=r+a)<51>(y:=c+b)>0and m[x][y]!='#'and{(x,y)}-v:v|={(x,y)};q+=(x,y,p+[(r,c)]),
