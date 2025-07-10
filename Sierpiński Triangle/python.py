t=[[' 'for _ in[0]*32]for _ in[0]*16]
def f(x,y,s):
 if s<2:t[y][x]='▲'
 else:n=s//2;f(x,y,n);f(x-n,y+n,n);f(x+n,y+n,n)
f(15,0,16)
for r in t:print(''.join(r))
