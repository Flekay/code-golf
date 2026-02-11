import sys
def solve(g):
 for r in range(9):
  for c in range(9):
   if g[r][c]<1:
    bx,by=r//3*3,c//3*3
    for n in range(1,10):
     if n not in g[r]and all(g[i][c]!=n for i in range(9))and all(g[i][j]!=n for i in range(bx,bx+3)for j in range(by,by+3)):
      g[r][c]=n
      if solve(g):return 1
    g[r][c]=0;return 0
 return 1
def sep(l,f,n,j,r):s=f*3;return l+(s+n+s+n+s+j)*2+s+n+s+n+s+r
for k,a in enumerate(sys.argv[1:]):
 if k:print()
 L=a.split('\n');g=[]
 for i in range(1,18,2):g.append([int(c)if c.isdigit()else 0 for c in L[i][2::4][:9]])
 solve(g)
 print(sep('┏','━','┯','┳','┓'))
 for i in range(9):
  s=''
  for j in range(9):s+=('┃'if j%3<1 else'│')+f' {g[i][j]} '
  print(s+'┃')
  if i<8:print(sep(*('┣━┿╋┫'if i%3==2 else'┠─┼╂┨')))
 print(sep('┗','━','┷','┻','┛'))
