import sys;j=22;q=0
for a,b in zip(b"E:E:E1=:=:",b"9F9F0F9>9>"):
 j-=2+(j==8)
 for i in range(a-49,b-49,a<b or-1):
  for c in(j,j-1)*(i!=6):q=q*2|(sys.argv[1][22*i+c]<'!')^i+c&1
exec("print(end=chr(q>>188&255));q<<=8;"*17)