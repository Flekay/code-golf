import sys
for x in sys.argv[1:]:
 a,n=map(int,x.split());j=1
 while a:
  while a%2<1:a//=2;j*=1-2*(n%8in(3,5))
  a,n=n,a;j*=1-2*(a%4>2<n%4);a%=n
 print(j*(n<2))
