import sys
for a in sys.argv[1:]:
 d,b=map(int,a.split());d//=2;B=b**d;n=(~-B**b//~-B)**d;s=0
 while n:s+=(n%B)**2;n//=B
 print(s)
