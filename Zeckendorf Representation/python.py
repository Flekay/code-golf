import sys
for n in map(int,sys.argv[1:]):
 while n:
  a=b=1
  while b<=n:a,b=b,a+b
  n-=a;print(a,end='\n'[n:]or' + ')
