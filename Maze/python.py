from sys import*;setrecursionlimit(9**9);*M,=argv[1]
I=M.index
def f(c):
 for d in-52,52,-1,1:
  if 2651>(n:=c+d)>-1and M[n]in' E':
   if n==I('E'):exit(print(*M,sep=''))
   M[n]='.';f(n);M[n]=' '
f(I('S'))
