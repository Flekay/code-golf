R,p=range,print
def s(g):
 def e():
  for r in R(9):
   for c in R(9):
    if g[r][c]<1:return r,c
 def v(n,w,l):
  if n in g[w]or n in[g[r][l]for r in R(9)]:return
  x,y=w//3*3,l//3*3
  if n in[g[r][c]for r in R(x,x+3)for c in R(y,y+3)]:return
  return 1
 def b():
  if not e():return 1
  r,c=e()
  for n in R(1,10):
   if v(n,r,c):
    g[r][c]=n
    if b():return 1
    g[r][c]=0
 b()
import sys
H,h,U,u,A,B,v='━─┯┷┿┼│';C=' {} '
H*=3;U=(H+U)*2;A=H+A;u=H+u;h*=3;B=h+B;v=C+v
s(b:=[[int(x)if x!='_'else 0for x in r]for r in sys.argv[1:]])
p("┏"+(U+H+'┳')*2+U+H+'┓')
for i,r in enumerate(b):p(("┃"+(v*2+C+'┃')*2+v*2+C+"┃").format(*[str(x)for x in r]));p("┣"+(A*2+H+'╋')*2+A*2+H+'┫'if i in(2,5)else"┠"+(B*2+h+'╂')*2+B*2+h+'┨'if i<8else"┗"+(u*2+H+'┻')*2+u*2+H+'┛')
