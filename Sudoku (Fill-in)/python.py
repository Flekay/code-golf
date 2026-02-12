import sys
R=range(9)
def f(p=0):
 while g[p]>' ':p+=1
 if p>80:return 1
 for n in{*'123456789'}-{*g[p-p%9:][:9],*g[p%9::9],*(g[p-p%27+p%9-p%3+i+i//3*6]for i in R)}:
  g[p]=n
  if f(p+1):return 1
 g[p]=' '
a=[*sys.argv[1]];g=[a[76*r+4*c+40]for r in R for c in R]+[''];f()
for p in range(81):a[4*p+40*-~(p//9)]=g[p]
print(*a,sep='')
