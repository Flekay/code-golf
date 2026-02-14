import sys;S=1;j=22;q=0
for t in[(20,8),(9,21)]*2+[(20,-1),(0,21)]+[(12,8),(9,13)]*2:
 S=-S;j-=2+(j==8)
 for i in range(*t,S):
  for c in(j,j-1)*(i!=6):q=q*2|(sys.argv[1][22*i+c]>' ')^i+c+1&1
exec("print(end=chr(q>>188&255));q<<=8;"*17)
