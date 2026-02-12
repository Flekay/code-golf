import sys
for a in sys.argv[1:]:
 s=p=j=0;m=[1]*99
 for c in a:
  if c>' ':m[1]+=c in"X/"and j<27;m[2]+=c=="X"and j<27;c=10if c=='X'else 10-p if c=='/'else int(c)if'/'<c<':'else ord(c)-9311if ord(c)>999else 0;s+=m.pop(0)*c;p=c
  j+=1
 print(s)
