import sys
for s in sys.argv[1:]:
 i=0
 while(c:=s[i:i+16]):print('%08x:'%i,'%-40s'%c.encode().hex(' ',-2),c.replace(*'\n.'));i+=16
 print()
