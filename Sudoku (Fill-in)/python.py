import sys
def f():
 try:p=g.index(' ')
 except:print(*a,sep='')
 for n in{*'123456789'}-{*g[p-p%9:][:9]+g[p%9::9]+[g[p-p%27+p%9-p%3+i+i//3*6]for i in range(9)]}:g[p]=a[q:=4*p+p//9*40+40]=n;f();g[p]=a[q]=' '
*a,=sys.argv[1];g=[a[4*i+i//9*40+40]for i in range(81)];f()