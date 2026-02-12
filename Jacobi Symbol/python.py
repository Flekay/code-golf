import sys
for x in sys.argv[1:]:
 a,n=map(int,x.split());s=0
 while a:
  while~a%2:a//=2;s^=n%8%6>2
  s^=a&2&n>1;a,n=n%a,a
 print((1|-s)*(n<2))
