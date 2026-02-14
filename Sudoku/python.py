R,p=range,print
def s(g):
 for r in R(9):
  for c in R(9):
   if g[r][c]<1:
    for n in R(1,10):
     if{n}-{*g[r],*[g[i][c]for i in R(9)],*[g[i][j]for i in R(r//3*3,r//3*3+3)for j in R(c//3*3,c//3*3+3)]}:
      g[r][c]=n
      if s(g):return 1
    g[r][c]=0;return
 return 1
import sys
H,h,U,u,A,B,v='━─┯┷┿┼│';C=' {} '
H*=3;U=(H+U)*2;A=H+A;u=H+u;h*=3;B=h+B;v=C+v
s(b:=[[x!='_'and int(x)for x in r]for r in sys.argv[1:]])
p("┏"+(U+H+'┳')*2+U+H+'┓')
for i,r in enumerate(b):p(("┃"+(v*2+C+'┃')*2+v*2+C+"┃").format(*r));p("┗"+(u*2+H+'┻')*2+u*2+H+'┛'if i>7else"┣"+(A*2+H+'╋')*2+A*2+H+'┫'if i%3>1else"┠"+(B*2+h+'╂')*2+B*2+h+'┨')
