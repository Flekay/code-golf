import sys
R=range(9)
def f():
 try:p=g.index(' ')
 except:
  for p in range(81):a[4*p+p//9*40+40]=g[p]
  exit(print(*a,sep=''))
 for n in{*'123456789'}-{*g[p-p%9:][:9],*g[p%9::9],*(g[p-p%27+p%9-p%3+i+i//3*6]for i in R)}:g[p]=n;f();g[p]=' '
*a,=sys.argv[1];g=[a[76*r+4*c+40]for r in R for c in R];f()