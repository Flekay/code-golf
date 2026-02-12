import sys
for x in sys.argv[1:]:
 a,n=map(int,x.split());j=1
 while a:
  while~a%2:a//=2;j*=n%8%6<3or-1
  a,n=n,a;j*=a%4&n%4<3or-1;a%=n
 print(j*(n<2))
