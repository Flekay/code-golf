from sys import*;setrecursionlimit(9**9);*M,=argv[1]
def f(c):
 for d in-52,52,-1,1:
  if M[n:=c+d]<'!':M[n]='.';f(n);M[n]=' '
  if'E'==M[n]:exit(print(*M,sep=''))
f(M.index('S'))